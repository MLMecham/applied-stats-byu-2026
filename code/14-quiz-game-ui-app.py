# 14-quiz-game-ui.py
# Deck 04: Beyond prompts (Tool calling UI)
# Goal: show tool activity in the app's UI:
#   1. register an "Update Score" tool with a title and icon (tool annotations)
#   2. record each graded answer in a reactive scores table
#   3. show running correct/incorrect tallies in value boxes

from typing import TypedDict

import chatlas
import dotenv
import polars as pl
from faicons import icon_svg
from pyhere import here
from shiny import App, reactive, render, ui

dotenv.load_dotenv()

# Goku power-up effect ---------------------------------------------------------
# Drop your own files in code/www/: goku.jpg (a .gif animates even better) and
# powerup.mp3. Or swap these src values for any URL you like.
GOKU_IMG = "/goku.jpg"
POWERUP_SOUND = "/powerup.mp3"

powerup_css = ui.tags.style("""
#powerup-overlay {
  position: fixed; inset: 0; z-index: 9999;
  display: flex; align-items: center; justify-content: center;
  pointer-events: none; opacity: 0;
}
#powerup-overlay .aura {
  position: absolute; width: 60vmin; height: 60vmin; border-radius: 50%;
  background: radial-gradient(circle,
    rgba(255,238,130,0.95) 0%, rgba(255,196,0,0.55) 40%, rgba(255,140,0,0) 70%);
  filter: blur(8px);
}
#powerup-overlay img {
  position: relative; width: min(360px, 60vw);
  filter: drop-shadow(0 0 20px gold);
}
#powerup-overlay.powerup-animate { animation: pu-flash 2s ease-out; }
#powerup-overlay.powerup-animate .aura { animation: pu-aura 2s ease-out; }
#powerup-overlay.powerup-animate img {
  animation: pu-zoom 2s ease-out, pu-shake 90ms linear 0s 14;
}
@keyframes pu-flash { 0%{opacity:0;} 12%{opacity:1;} 78%{opacity:1;} 100%{opacity:0;} }
@keyframes pu-zoom { 0%{transform:scale(.2);} 45%{transform:scale(1.15);} 100%{transform:scale(1);} }
@keyframes pu-aura {
  0%{transform:scale(.2);opacity:0;} 40%{transform:scale(1.2);opacity:1;} 100%{transform:scale(1.6);opacity:0;}
}
@keyframes pu-shake { 0%,100%{margin-left:0;} 25%{margin-left:-10px;} 75%{margin-left:10px;} }
""")

powerup_js = ui.tags.script("""
Shiny.addCustomMessageHandler("powerup", function(message) {
  var overlay = document.getElementById("powerup-overlay");
  var audio = document.getElementById("powerup-audio");
  if (!overlay) return;
  // Restart the animation even if it just fired.
  overlay.classList.remove("powerup-animate");
  void overlay.offsetWidth;
  overlay.classList.add("powerup-animate");
  overlay.addEventListener("animationend", function handler() {
    overlay.classList.remove("powerup-animate");
    overlay.removeEventListener("animationend", handler);
  });
  if (audio) { try { audio.currentTime = 0; audio.play(); } catch (e) {} }
});
""")

powerup_overlay = ui.tags.div(
    ui.tags.div(class_="aura"),
    ui.tags.img(src=GOKU_IMG, alt="Power up!"),
    id="powerup-overlay",
)
powerup_audio = ui.tags.audio(id="powerup-audio", src=POWERUP_SOUND, preload="auto")

# UI ---------------------------------------------------------------------------

app_ui = ui.page_sidebar(
    ui.sidebar(
        ui.value_box(
            "Correct Answers",
            ui.output_text("txt_correct"),
            showcase=icon_svg("circle-check"),
            theme="success",
        ),
        ui.value_box(
            "Incorrect Answers",
            ui.output_text("txt_incorrect"),
            showcase=icon_svg("circle-xmark"),
            theme="danger",
        ),
        position="right",
        fillable=True,
        width=400,
    ),
    ui.head_content(powerup_css, powerup_js),
    ui.navset_card_underline(
        ui.nav_panel(
            "Quiz Game",
            ui.chat_ui("chat"),
        ),
        ui.nav_panel(
            "Your Answers",
            ui.output_data_frame("tbl_score"),
        ),
    ),
    powerup_overlay,
    powerup_audio,
    title="Quiz Game",
    fillable=True,
)


class QuestionAnswer(TypedDict):
    theme: str
    question: str
    answer: str
    your_answer: str
    is_correct: bool


def server(input, output, session):
    chat_ui = ui.Chat(id="chat")

    # Set up the chat instance
    client = chatlas.ChatAnthropic(
        model="claude-sonnet-4-6",
        system_prompt=f"""
{here("code/11-quiz-game-prompt.md").read_text(encoding="utf-8")}

After every question, use the "Update Score" tool to keep track of the user's
score. Be sure to call the tool after you have graded the user's final answer to
the question.
""",
    )

    scores = reactive.value[list[QuestionAnswer]]([])
    # Bumped on each correct answer; the effect below fires the Goku power-up.
    powerup = reactive.value(0)

    @reactive.effect
    async def _powerup():
        n = powerup()
        if n > 0:
            await session.send_custom_message("powerup", {"n": n})

    @render.data_frame
    def tbl_score():
        df = pl.DataFrame(scores())
        return df

    @render.text
    def txt_correct() -> int:
        return len([d for d in scores() if d["is_correct"]])

    @render.text
    def txt_incorrect() -> int:
        return len([d for d in scores() if not d["is_correct"]])

    def update_score(
        theme: str,
        question: str,
        answer: str,
        your_answer: str,
        is_correct: bool,
    ):
        """
        Add a correct or incorrect answer to the score. Call this tool after
        you've graded the user's answer to a question.

        Parameters
        ----------
        theme: The theme of the round.
        question: The quiz question that was asked.
        answer: The correct answer to the question.
        your_answer: The user's answer to the question.
        is_correct: Whether the user's answer was correct.
        """
        with reactive.isolate():
            val_scores = scores.get()

        answer = QuestionAnswer(
            theme=theme,
            question=question,
            answer=answer,
            your_answer=your_answer,
            is_correct=is_correct,
        )

        val_scores = [*val_scores, answer]
        scores.set(val_scores)

        # Fire the power-up animation + sound on a correct answer.
        if is_correct:
            powerup.set(powerup.get() + 1)

        correct = len([d for d in val_scores if d["is_correct"]])
        incorrect = len(val_scores) - correct
        return {"correct": correct, "incorrect": incorrect}

    client.register_tool(
        update_score,
        annotations={
            "title": "Update Score",
            "extra": {"icon": icon_svg("circle-plus")},
        },
    )

    @chat_ui.on_user_submit
    async def handle_user_input(user_input: str):
        response = await client.stream_async(user_input, content="all")
        await chat_ui.append_message_stream(response)

    @reactive.effect
    def _():
        chat_ui.update_user_input(value="Let's play the quiz game!", submit=True)


app = App(app_ui, server, static_assets=str(here("code/www")))

# 11-quiz-game-app.R
# Deck 03: Prompt engineering and RAG (Prompt engineering and hallucinations)
# Goal: write the system prompt for the quiz game show. Iterate on it and test
# against a few user messages.

library(shiny)
library(bslib)
library(ellmer)
library(shinychat)

# UI ---------------------------------------------------------------------------

ui <- page_fillable(
  chat_mod_ui("chat")
)

# Server -----------------------------------------------------------------------

server <- function(input, output, session) {
  client <- chat(
    "anthropic/claude-sonnet-4-6",
    system_prompt = interpolate_file(
      here::here("code/11-quiz-game-prompt.md")
    )
  )

  chat <- chat_mod_server("chat", client)

  observe({
    # Start the game when the app launches
    chat$update_user_input(
      value = "Let's play the quiz game!",
      submit = TRUE
    )
  })
}

shinyApp(ui, server)

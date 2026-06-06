# 15-quiz-game-ui.py
# Deck 04: Beyond prompts (Tool calling UI)
# Goal: progressively upgrade the quiz show app:
#   1. add tool annotations to give play_sound an icon and title
#   2. return a ContentToolResult with custom title and icon
#   3. track answers and score in reactive value boxes that update from tools

from shiny import App, ui, reactive
import chatlas

# TODO: build on 15-quiz-game-tools.py and add the three upgrades above

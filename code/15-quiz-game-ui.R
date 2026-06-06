# 15-quiz-game-ui.R
# Deck 04: Beyond prompts (Tool calling UI)
# Goal: progressively upgrade the quiz show app:
#   1. add tool annotations to give play_sound an icon and title
#   2. return a ContentToolResult with custom title and icon
#   3. track answers and score in reactive value boxes that update from tools

library(shiny)
library(shinychat)
library(ellmer)
library(bslib)

# TODO: build on 15-quiz-game-tools.R and add the three upgrades above

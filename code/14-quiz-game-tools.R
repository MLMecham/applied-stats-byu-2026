# 14-quiz-game-tools.R
# Slide 03: Augmented generation (Tool calling)
# Goal: Shiny quiz show app. We provide a function that plays a sound via
# beepr; document it well and register it as a tool the model can call.

library(shiny)
library(shinychat)
library(ellmer)
library(beepr)

# TODO: write play_sound(name) with a clear docstring covering allowed names
# TODO: register play_sound as a tool on the chat object
# TODO: build a minimal Shiny app that uses the chat

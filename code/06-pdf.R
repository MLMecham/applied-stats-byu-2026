# 06-pdf.R
# Deck 02: Programming with LLMs (Multi-modal input)
# Goal: pass a PDF recipe and turn it into clean Markdown.

# %% Import package
library(ellmer)

# %% Read in a recipe PDF
recipe_pdfs <- here::here("data/recipes/pdf")
pdf_waffles <- file.path(recipe_pdfs, "CinnamonPeachOatWaffles.pdf")

# %% Pass the PDF to the chat and ask for ingredients and steps
chat <- chat_anthropic()
chat$chat(
  "Summarize the recipe in this PDF into a list of ingredients and the steps to follow to make the recipe.",
  content_pdf_file(pdf_waffles)
)

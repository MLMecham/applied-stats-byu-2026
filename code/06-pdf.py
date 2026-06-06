# 06-pdf.py
# Deck 02: Programming with LLMs (Multi-modal input)
# Goal: pass a PDF recipe and turn it into clean Markdown.

# %% Import packages and load environment variable for API access
import chatlas
import dotenv
from pyhere import here

dotenv.load_dotenv()

# %% Read in a recipe PDF
recipe_pdfs = here("data/recipes/pdf/")
pdf_cheesesteak = recipe_pdfs / "PhillyCheesesteak.pdf"

# %% Pass the PDF to the chat and ask for ingredients and steps
chat = chatlas.ChatAnthropic()
chat.chat(
    "Summarize the recipe in this PDF into a list of ingredients "
    "and the steps to follow to make the recipe.",
    chatlas.content_pdf_file(pdf_cheesesteak),
)

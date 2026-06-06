# 03-live.py
# Deck 01: Talking with LLMs via code (Shinychat basics)
# Goal: launch a live chat UI against an existing chat object using
# chat.console() and chat.app().

# %% Import packages and create chat
import chatlas
import dotenv
dotenv.load_dotenv()
chat = chatlas.ChatAnthropic()

# %% Converse with the chatbot in your console
chat.console()

# %% After a bit, exit the chat and try chatting in a Shiny app.
chat.app()

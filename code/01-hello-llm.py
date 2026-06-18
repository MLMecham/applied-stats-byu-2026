# 01-hello-llm.py
# Deck 01: Talking with LLMs via code (Set-up and verify API access)

# %% Import packages and load environment variable for API access

import chatlas
import dotenv

dotenv.load_dotenv()

# %% Verify API access by writing a short poem about SIAS 2026
chat = chatlas.ChatAnthropic()
chat.chat(
    "I'm at SIAS 2026 to learn about programming with LLMs and chatlas!",
    "Write a short poem or limerick to celebrate.",
)

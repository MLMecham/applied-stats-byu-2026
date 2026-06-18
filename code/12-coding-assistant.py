# 12-coding-assistant.py
# Deck 03: Prompt engineering and RAG (Manual RAG)
# Goal: ask the LLM to write a function using a niche package, first with no
# context and then with the package README pasted into the prompt. Compare.

# %% setup
import chatlas
import dotenv
from pyhere import here

dotenv.load_dotenv()

# %% [markdown]
# **Step 1:** Run the code below as-is to try the task without any extra
# context. How does the model do? Does it know enough about the NWS Python
# package to complete the task?
#
# **Step 2:** Now, let's add some context. Head over to the GitHub Repo for NWS
# (link in `12-coding-assistant-docs-py.md`). Copy the project description from
# the `README.md` and paste it into `12-coding-assistant-docs-py.md`.
#
# **Step 3:** Uncomment the extra lines to include these docs in the prompt and
# try again.

# %% task
chat = chatlas.ChatAuto("anthropic/claude-sonnet-4-6")

chat.chat(
    # Step 3: uncomment to add the package docs as context
    # here("code/12-coding-assistant-docs-py.md").read_text(encoding="utf-8"),
    # Task prompt
    "Write a simple function that takes latitude and longitude as inputs "
    "and returns the weather forecast for that location using the NWS "
    "package. Keep the function concise and simple and don't include error "
    "handling or data re-formatting. Include a short docstring, including "
    "examples for NYC and Atlanta, GA."
    "No new packages",
)


# %% [markdown]
# Put the result from the model in code block below to try it out.

# %% results
import requests


def get_weather_forecast(lat: float, lon: float) -> dict:
    """
        Returns the weather forecast for a given latitude and longitude using
    the NWS API.

        Examples:
            NYC:     get_weather_forecast(40.7128, -74.0060)
            Atlanta: get_weather_forecast(33.7490, -84.3880)
    """
    points_url = f"https://api.weather.gov/points/{lat},{lon}"
    forecast_url = requests.get(points_url).json()["properties"]["forecast"]

    return requests.get(forecast_url).json()["properties"]["periods"]


# %%

print(get_weather_forecast(40.7128, -74.0060))

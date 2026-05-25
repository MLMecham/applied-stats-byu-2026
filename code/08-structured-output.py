# 08-structured-output.py
# Slide 02: Programming with LLMs (Structured output)
# Goal: extract structured fields (ingredients, steps, yield, prep time) from a
# recipe PDF using a Pydantic model with chatlas.

from pydantic import BaseModel, ConfigDict
import chatlas

# TODO: define a Pydantic Recipe model (consider use_attribute_docstrings=True)
# TODO: call chat.extract_data() against the recipe PDF

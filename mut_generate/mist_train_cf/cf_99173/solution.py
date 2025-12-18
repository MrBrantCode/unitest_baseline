"""
QUESTION:
Create a Python function named `my_function` that takes a JSON string as input, parses it, and returns a new JSON string as output. The input JSON string contains a person's name and age, and the output JSON string should contain a personalized greeting message.
"""

import json

def my_function(inputs):
    inputs = json.loads(inputs)
    name = inputs["name"]
    age = inputs["age"]
    return {
        "greeting": f"Hello {name}! You are {age} years old."
    }
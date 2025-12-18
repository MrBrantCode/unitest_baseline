"""
QUESTION:
Create a function `my_function` that takes a JSON string `inputs` as input, parses it, and returns a JSON object with a greeting message. The `inputs` JSON object contains two keys: `name` and `age`. The greeting message should be in the format "Hello {name}! You are {age} years old." and should be stored in a key called `greeting`.
"""

import json

def my_function(inputs):
    inputs = json.loads(inputs)
    name = inputs["name"]
    age = inputs["age"]
    return {
        "greeting": f"Hello {name}! You are {age} years old."
    }
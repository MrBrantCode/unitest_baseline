"""
QUESTION:
Create a function `validate_model_name` that takes a string `model_name` as input. The function should return "Invalid model name" if the `model_name` starts with a digit, otherwise, it should return "Valid model name". The model name is a string that can contain alphanumeric characters and underscores.
"""

def validate_model_name(model_name):
    if model_name[0].isdigit():  # Check if the first character is a digit
        return "Invalid model name"
    else:
        return "Valid model name"
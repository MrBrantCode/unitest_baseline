"""
QUESTION:
Create a function `predict` that takes a list of values as input and returns a list of classifications for each value, either 0 or 1. The input list contains floating-point numbers and each number is wrapped in a sublist.
"""

def predict(values):
    # assuming model is a pre-trained model, replace with actual model implementation
    return [1 if value[0] > 1 else 0 for value in values]
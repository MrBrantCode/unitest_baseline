"""
QUESTION:
Create a function called `calculate_variance_and_std` that takes a list of numbers as input and returns the variance and standard deviation of the list. The function should manually calculate the variance and standard deviation without using any built-in Python libraries. The input list should only contain integer or float values, and the function should include error-checking to enforce this restriction.
"""

def calculate_variance_and_std(data):
    if isinstance(data, list) and all(isinstance(i, (int, float)) for i in data):
        mean = sum(data) / len(data)
        variance = sum((i - mean) ** 2 for i in data) / len(data)
        std_dev = variance ** 0.5
        return variance, std_dev
    else:
        return "Input should be a list of integer or float values"
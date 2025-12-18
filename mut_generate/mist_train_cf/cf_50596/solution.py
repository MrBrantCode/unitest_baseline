"""
QUESTION:
Create a function `get_result(x)` that takes an integer `x` as input and returns its corresponding string representation without using "if-else" or "switch" statements. The function should be scalable to easily accommodate the addition of new number-string pairs. If the input number does not have a corresponding string representation, the function should return "other".
"""

def get_result(x):
    """
    Function to get the string value of a number. Returns the string from the dictionary if it exists else it returns 'other'.
    """
    numbers_dict = {
        0: "zero",
        1: "one",
    }
    return numbers_dict.get(x, "other")
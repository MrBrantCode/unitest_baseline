"""
QUESTION:
Write a function `convert_array_to_string` that takes an array of 12 integers ranging from -100 to 355 and returns a string representation of the array, excluding any integers divisible by 5.
"""

def convert_array_to_string(arr):
    result = ""
    for num in arr:
        if num % 5 != 0:
            result += str(num) + " "
    return result.strip()  # Remove trailing whitespace
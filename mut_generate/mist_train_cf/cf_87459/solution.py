"""
QUESTION:
Create a function named `calculate_frequency` that takes a list of numbers (including integers and floating-point numbers) as an argument and returns a dictionary containing the frequency of each number with precision up to 2 decimal places for floating-point numbers. The function should have a time complexity of O(n), where n is the number of elements in the input list, and a space complexity of O(m), where m is the number of unique elements in the input list. The function should not use the built-in `collections` module or any other external libraries.
"""

def calculate_frequency(numbers):
    frequency = {}
    for num in numbers:
        key = "{:.2f}".format(num)
        if key in frequency:
            frequency[key] += 1
        else:
            frequency[key] = 1
    return frequency
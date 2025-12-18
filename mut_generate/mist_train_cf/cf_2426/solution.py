"""
QUESTION:
Create a function called `calculate_frequency` that takes a list of numbers as input and returns a dictionary containing the frequency of each number. The function should handle both integers and floating-point numbers with precision up to their full decimal representation. The function should not use any external libraries, have a time complexity of O(n), and a space complexity of O(m), where n is the number of elements in the input list and m is the number of unique elements.
"""

def calculate_frequency(numbers):
    frequency = {}
    for num in numbers:
        key = str(num)
        if key in frequency:
            frequency[key] += 1
        else:
            frequency[key] = 1
    return frequency
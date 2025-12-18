"""
QUESTION:
Implement a function named `create_frequency_map` that takes a list of numbers as input and returns a data structure where the numbers are the keys and their frequencies are the values. The function should return a dictionary where each key is a number from the input list and its corresponding value is the number of times the number appears in the list.
"""

def create_frequency_map(numbers):
    frequency_map = {}
    for num in numbers:
        if num in frequency_map:
            frequency_map[num] += 1
        else:
            frequency_map[num] = 1
    return frequency_map
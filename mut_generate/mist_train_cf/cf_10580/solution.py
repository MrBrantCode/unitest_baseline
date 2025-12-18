"""
QUESTION:
Create a function named `frequency_counter` that takes a list of integers as an argument. The function should return a dictionary containing the frequency of each non-zero occurrence of numbers in the list. The function must have a time complexity of O(n), where n is the number of elements in the input list.
"""

def frequency_counter(numbers):
    frequency = {}
    for number in numbers:
        if number in frequency:
            frequency[number] += 1
        else:
            frequency[number] = 1
    return {key: value for key, value in frequency.items() if value != 0}
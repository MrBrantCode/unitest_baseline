"""
QUESTION:
Write a function `remove_extremes(input_string)` that takes a string of comma-separated numbers, removes the two largest values and the two smallest values from the string, and returns a new string with the remaining values.
"""

def remove_extremes(input_string):
    numbers = input_string.split(", ")
    numbers = [int(num) for num in numbers]
    numbers.sort()
    numbers = numbers[2:-2]
    numbers = [str(num) for num in numbers]
    return ", ".join(numbers)
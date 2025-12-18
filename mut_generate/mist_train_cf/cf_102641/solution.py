"""
QUESTION:
Write a function called `find_min_max` that takes a list of numbers as input and returns a tuple containing the minimum and maximum values in the list. The list will always have at least 5 numbers, may contain duplicates, and you cannot use built-in functions like `min()` and `max()`.
"""

def find_min_max(numbers):
    minimum = numbers[0]
    maximum = numbers[0]
    
    for num in numbers:
        if num < minimum:
            minimum = num
        if num > maximum:
            maximum = num
    
    return minimum, maximum
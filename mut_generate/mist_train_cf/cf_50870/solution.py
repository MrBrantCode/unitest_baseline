"""
QUESTION:
Write a function `correct_intersperse(numbers, delimiter)` that takes a list of numbers and a delimiter as input, and returns a new list with the delimiter inserted between every two consecutive elements. The function should not append the delimiter after the last element.
"""

def correct_intersperse(numbers, delimiter):
    result = []
    for i in range(len(numbers)):
        result.append(numbers[i])
        if i != len(numbers) - 1:  # Not to append delimiter after the last element
            result.append(delimiter)
    return result
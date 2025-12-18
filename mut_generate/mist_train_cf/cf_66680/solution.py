"""
QUESTION:
Write a function named `intersperse` that takes three parameters: two lists of integers (`numbers1` and `numbers2`) and an integer `delimiter`. The function should interweave `numbers1` and `numbers2` with the `delimiter` in between each pair of numbers. If `delimiter` is negative, use its absolute value. If `numbers1` and `numbers2` are of different lengths, append the remaining elements of the longer list, each followed by the `delimiter`. Remove the last `delimiter` from the result.
"""

from typing import List

def intersperse(numbers1: List[int], numbers2: List[int], delimiter: int) -> List[int]:
    if delimiter < 0:
        delimiter = abs(delimiter)
    try:
        numbers1.pop(delimiter)
        numbers2.pop(delimiter)
    except IndexError:
        pass  

    result = []
    for num1, num2 in zip(numbers1, numbers2):
        result.extend([num1, delimiter, num2, delimiter])

    if len(numbers1) > len(numbers2):
        for num in numbers1[len(numbers2):]:
            result.extend([num, delimiter])

    elif len(numbers2) > len(numbers1):
        for num in numbers2[len(numbers1):]:
            result.extend([num, delimiter])

    return result[:-1]
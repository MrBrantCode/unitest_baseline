"""
QUESTION:
Design a function `find_ascii` that takes two parameters: a list of numbers and an integer `k`. The function should return the ASCII character corresponding to the `k`th smallest number in the list after sorting it in ascending order. If `k` is greater than the length of the list, the function should return an error message.
"""

def find_ascii(numbers, k):
    if k > len(numbers):
        return "Error: k is greater than the length of the list."
    else:
        numbers.sort()
        return chr(numbers[k-1])
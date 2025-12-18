"""
QUESTION:
Write a function `get_even_numbers` that takes in a list of integers `lst`, and optionally a range defined by `start` and `end` indices (defaulting to 4 and 8, respectively), as well as a boolean parameter `even` (defaulting to True) to indicate whether to retrieve even or odd numbers. The function should return a list of numbers from the specified range in the list that match the parity indicated by the `even` parameter.
"""

def get_even_numbers(lst, start=4, end=8, even=True):
    even_numbers = []
    for i in range(start, end+1):
        if (even and lst[i] % 2 == 0) or (not even and lst[i] % 2 != 0):
            even_numbers.append(lst[i])
    return even_numbers
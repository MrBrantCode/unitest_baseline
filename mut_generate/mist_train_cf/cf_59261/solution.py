"""
QUESTION:
Create a function called `recursive_intersperse` that takes a list of integers `numbers` and an integer `delimeter` as input. The function should return a new list where the `delimeter` is inserted between every two consecutive elements of `numbers`. Implement the function using recursion. Do not use loops.
"""

def recursive_intersperse(numbers, delimeter):
    if len(numbers) == 0:
        return []
    elif len(numbers) == 1:
        return [numbers[0]]
    else:
        return [numbers[0], delimeter] + recursive_intersperse(numbers[1:], delimeter)
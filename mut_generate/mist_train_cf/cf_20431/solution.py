"""
QUESTION:
Implement a function `find_minimum` that takes a list of numbers as input and returns the minimum value in the list. The function should use recursion, have a time complexity of O(n), and only use constant space. It should not utilize any built-in sorting or searching functions.
"""

def find_minimum(numbers):
    if len(numbers) == 1:
        return numbers[0]
    if len(numbers) == 2:
        return min(numbers[0], numbers[1])

    mid = len(numbers) // 2
    left_min = find_minimum(numbers[:mid])
    right_min = find_minimum(numbers[mid:])

    return min(left_min, right_min)
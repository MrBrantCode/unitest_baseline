"""
QUESTION:
Implement the function `find_minimum(numbers)` that takes a list of numbers as input and returns the minimum value in the list, subject to the following constraints:

- The function should be implemented using recursion.
- The function should have a time complexity of O(n) where n is the length of the input.
- The function should not use any built-in sorting or searching functions.
- The function should be implemented using only constant space, i.e., no additional data structures should be used apart from the input and output variables.
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
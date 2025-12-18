"""
QUESTION:
Create a function `generate_fibonacci(n)` that generates an array of `n` elements, where each element is the sum of its two preceding elements, with the first two elements being 0 and 1. The function should have a time complexity of O(n) and a space complexity of O(1), excluding the space required for the output array.
"""

def entrance(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    result = [0, 1]
    for i in range(2, n):
        result.append(result[i - 1] + result[i - 2])

    return result
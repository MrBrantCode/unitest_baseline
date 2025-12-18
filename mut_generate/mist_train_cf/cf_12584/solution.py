"""
QUESTION:
Create a function `list_comprehension` that uses list comprehension to generate a list of squares of even numbers from 1 to n. The function should take an integer `n` as input and return a list of squares of even numbers in the range 1 to `n` (inclusive). The function should have a time complexity of O(n) and a space complexity of O(m), where m is the number of even numbers in the range 1 to `n`.
"""

def list_comprehension(n):
    return [x**2 for x in range(1, n+1) if x % 2 == 0]
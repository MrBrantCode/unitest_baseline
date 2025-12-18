"""
QUESTION:
Write a function `generate_list(n)` that generates a list of length n containing all numbers from 1 to n without using any built-in functions or libraries. The function should have a time complexity of O(n) and a space complexity of O(1), excluding the space required for the output list.
"""

def generate_list(n):
    numbers = []
    for i in range(1, n + 1):
        numbers.append(i)
    return numbers
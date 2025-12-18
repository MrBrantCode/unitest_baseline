"""
QUESTION:
Write a function called `generate_odd_squares` that generates an array of length n containing the squares of odd numbers from 1 to n, excluding any number that is divisible by 3. The function should take one integer parameter `n` and return a list of integers.
"""

def generate_odd_squares(n):
    result = []
    for i in range(1, n+1):
        if i % 2 != 0 and i % 3 != 0:
            result.append(i**2)
    return result
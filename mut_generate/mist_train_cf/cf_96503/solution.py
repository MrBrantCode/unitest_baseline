"""
QUESTION:
Generate a function named `multiples` that creates a list of all multiples of 3 and 5 from 0 to a given number `n`, excluding any numbers that are also multiples of 7. The solution should have a time complexity of O(n) and should not use any built-in functions or libraries to check for multiples.
"""

def multiples(n):
    result = []
    for num in range(n + 1):
        if num % 3 == 0 or num % 5 == 0:
            if num % 7 != 0:
                result.append(num)
    return result
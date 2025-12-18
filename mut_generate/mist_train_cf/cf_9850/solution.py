"""
QUESTION:
Create a function called `generate_reverse_list` that generates a list of numbers from 1 to n in reverse order. The function should take an integer n as input and return a list of integers from n down to 1.
"""

def generate_reverse_list(n):
    return list(range(n, 0, -1))
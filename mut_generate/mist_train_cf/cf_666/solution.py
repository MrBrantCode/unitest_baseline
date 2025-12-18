"""
QUESTION:
Generate a function `generate_squares_dict(n)` that creates a dictionary containing the squares of numbers from 1 to n (1 ≤ n ≤ 100), with unique square values, string keys in ascending order, and a time complexity less than O(n*log(n)) and a space complexity less than O(n).
"""

def generate_squares_dict(n):
    squares_dict = {}
    for i in range(1, n+1):
        squares_dict[str(i)] = i**2
    return squares_dict
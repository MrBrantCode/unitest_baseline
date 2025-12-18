"""
QUESTION:
Create a function named `generate_list` that takes two integers `n` and `m` as parameters. The function should return a list containing numbers from `n` to `m` (not including `m`) if both `n` and `m` are positive and `n` is less than `m`. Otherwise, it should return "Invalid input".
"""

def generate_list(n, m):
    if n >= m or n < 0 or m < 0:
        return "Invalid input"
    else:
        return list(range(n, m))
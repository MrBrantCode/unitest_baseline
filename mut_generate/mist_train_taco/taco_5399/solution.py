"""
QUESTION:
Example

Input

3
3 0 1


Output

2
"""

def find_missing_number(n, numbers):
    i = 0
    while i <= n:
        if str(i) not in numbers:
            return i
        i += 1
    return -1  # This line should never be reached if the input is valid
"""
QUESTION:
Create a function `create_array(n)` that generates an array of integers from `n-1` down to `0` without using any built-in array creation or reversal functions. The input `n` is a positive integer that can be as large as 10^9. The function should have a time complexity of O(n).
"""

def create_array(n):
    arr = []
    for i in range(n-1, -1, -1):
        arr.append(i)
    return arr
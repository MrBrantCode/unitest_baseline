"""
QUESTION:
Write a function `is_palindromic(arr)` that determines if a given two-dimensional array represents a palindromic sequence both row-wise and column-wise. The array must have an odd length when combined row-wise or column-wise. Implement this function without using any additional data structures, and ensure it can handle arrays of varying lengths (up to N dimensions where N > 2).
"""

def is_palindromic(arr):
    # Step1: Check if the array and sub-array length is odd
    n = len(arr)
    m = len(arr[0])
    if n % 2 == 0 or m % 2 == 0:
        return False

    # Step2: Check each row
    for row in arr:
        if row != row[::-1]:
            return False

    # Step3: Check each column
    for i in range(m):
        col = [arr[j][i] for j in range(n)]
        if col != col[::-1]:
            return False

    return True
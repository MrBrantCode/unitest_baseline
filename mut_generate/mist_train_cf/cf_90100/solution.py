"""
QUESTION:
Write a function called `square_root(n)` to calculate the floor value of the square root of a given positive integer `n` using only integer operations, with a time complexity of O(log n) and without using any built-in square root functions or external libraries.
"""

def square_root(n):
    # Base cases
    if n == 0 or n == 1:
        return n

    # Binary search
    start = 1
    end = n
    while start <= end:
        mid = (start + end) // 2

        # If mid is the square root, return mid
        if mid * mid == n:
            return mid

        # If mid^2 is less than n, search in the right half
        if mid * mid < n:
            start = mid + 1
            result = mid  # Store the floor value of the square root

        # If mid^2 is greater than n, search in the left half
        else:
            end = mid - 1

    return result
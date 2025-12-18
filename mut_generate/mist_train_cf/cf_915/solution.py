"""
QUESTION:
Create a function `is_perfect_square(n)` and `calculate_square_root(n)` to determine if a given number `n` is a perfect square and calculate its square root, respectively, without using built-in functions or libraries. The function should return a boolean value for `is_perfect_square(n)` and the square root value for `calculate_square_root(n)`. The function should handle negative numbers and non-numeric inputs by returning an error message. The time complexity of the solution should be O(log n).
"""

def is_perfect_square(n):
    if not isinstance(n, (int, float)):
        return "Error: Invalid input"

    if n < 0:
        return False

    if n == 0:
        return True

    low, high = 1, n // 2

    while low <= high:
        mid = (low + high) // 2
        square = mid * mid

        if square == n:
            return True
        elif square > n:
            high = mid - 1
        else:
            low = mid + 1

    return False


def calculate_square_root(n):
    if not isinstance(n, (int, float)):
        return "Error: Invalid input"

    if n < 0:
        return "Error: Cannot calculate square root of a negative number"

    if n == 0:
        return 0

    low, high = 0, n

    while low <= high:
        mid = (low + high) / 2
        square = mid * mid

        if abs(square - n) < 0.0001:  # Consider a small difference as an approximation
            return mid
        elif square > n:
            high = mid
        else:
            low = mid

    return "Error: Unable to calculate square root"
"""
QUESTION:
Write a function `calculate_e(n)` in Python to calculate the value of "e" to 4 decimal places without using any built-in math functions or libraries. The function should be able to handle large inputs and efficiently compute the value of "e" within a reasonable time frame. The function should return "Invalid input" if `n` is less than 0, and it should return the result as a float.
"""

def calculate_e(n):
    if n < 0:
        return "Invalid input"
    elif n == 0:
        return 1
    else:
        result = 1
        factorial = 1
        for i in range(1, n+1):
            factorial *= i
            result += 1/factorial
        return round(result, 4)
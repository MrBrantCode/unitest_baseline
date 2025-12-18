"""
QUESTION:
Write a function `fibonacci_sequence(num)` to generate the Fibonacci sequence up to a given number `num`. The function should handle negative input values by returning an error message. The time complexity should be O(n), where n is the input number, and the space complexity should be O(1).
"""

def fibonacci_sequence(num):
    if num < 0:
        print("Error! Input number should be positive")
        return None

    a, b = 0, 1
    while b <= num:
        print(b, end=" ")
        a, b = b, a + b
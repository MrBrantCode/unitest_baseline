"""
QUESTION:
Create a function called `fibonacci_sequence` that takes a positive integer `num` as input. The function generates and prints the Fibonacci sequence up to the given number `num`. The time complexity of the function should be O(n) and space complexity should be O(1), where n is the input number. If the input number is negative, the function should print an error message and return `None`.
"""

def fibonacci_sequence(num):
    if num < 0:
        print("Error! Input number should be positive")
        return None

    # Initializing the first two Fibonacci numbers
    a, b = 0, 1

    # Generating Fibonacci sequence up to the given number
    while b <= num:
        print(b, end=" ")
        a, b = b, a + b
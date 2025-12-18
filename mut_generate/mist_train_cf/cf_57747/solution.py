"""
QUESTION:
Create a Python function named `check_value` that takes one integer parameter `n` and prints a message based on whether the value of `n` is 0 or not. The function should be called from another function named `main`. Implement exception handling in the `main` function to catch any potential errors that may occur during execution. Ensure that the code is readable and maintainable by dividing tasks into separate functions. Define the value of `n` in the `main` function before calling `check_value`.
"""

def check_value(n):
    if n == 0:
        return "Hey I'm there"
    else:
        return "The variable 'n' is not equal to zero"
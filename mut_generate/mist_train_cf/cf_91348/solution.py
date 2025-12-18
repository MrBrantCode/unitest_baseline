"""
QUESTION:
Write a function named `print_string` that takes a string and a non-negative integer as input, and prints the string the specified number of times using recursion. The function should handle cases where the input number is zero or negative by not printing anything.
"""

def print_string(string, num):
    if num <= 0:  # base case: stop recursion when num is zero or negative
        return
    print(string)  # print the string
    print_string(string, num - 1)  # recursively call the function with num decremented by 1
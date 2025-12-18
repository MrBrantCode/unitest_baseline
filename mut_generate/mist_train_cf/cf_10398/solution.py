"""
QUESTION:
Write a function called `print_string` that takes two parameters, a string and a number. The function should print the string the number of times specified by the number using recursion. The function should handle cases where the number is zero or negative by not printing anything.
"""

def entrance(string, num):
    if num <= 0:  # base case: stop recursion when num is zero or negative
        return
    print(string)  # print the string
    entrance(string, num - 1)  # recursively call the function with num decremented by 1
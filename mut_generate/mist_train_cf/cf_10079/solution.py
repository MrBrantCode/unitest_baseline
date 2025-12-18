"""
QUESTION:
Implement a function `is_palindrome(string)` that checks whether a given string is a palindrome (reads the same forwards and backwards). The function should use both a stack and a queue data structure to solve the problem, have a time complexity of O(n), and include error handling for potential edge cases, such as empty stack or queue. The input string may contain spaces, and the function should ignore case sensitivity.
"""

def is_palindrome(string):
    string = string.lower().replace(" ", "")  # Convert to lowercase and remove spaces
    stack = []
    queue = []

    for char in string:
        stack.append(char)
        queue.append(char)

    while len(stack) > 0:
        if stack.pop() != queue.pop(0):
            return False

    return True
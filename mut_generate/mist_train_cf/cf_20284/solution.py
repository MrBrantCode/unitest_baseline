"""
QUESTION:
Write a function named `reverse_string` that takes a string `s` as input and returns the reversed string without using built-in library functions or additional data structures. The solution should have a time complexity of O(n) and a space complexity of O(1), and it should be implemented recursively.
"""

def reverse_string(s):
    # Base case: if string is empty or has only one character, return the string
    if len(s) <= 1:
        return s
    
    # Recursive case: reverse the substring excluding the first character, and append the first character to the end
    return reverse_string(s[1:]) + s[0]
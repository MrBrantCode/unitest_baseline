"""
QUESTION:
Implement a function named `reverse_string(s)` that takes a string `s` as input and returns the reversed string. The function must have a time complexity of O(n), where n is the length of the input string, and a space complexity of O(1). The implementation should be recursive and should not use any built-in library functions or additional data structures.
"""

def reverse_string(s):
    # Base case: if string is empty or has only one character, return the string
    if len(s) <= 1:
        return s
    
    # Recursive case: reverse the substring excluding the first character, and append the first character to the end
    return reverse_string(s[1:]) + s[0]
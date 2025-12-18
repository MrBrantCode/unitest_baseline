"""
QUESTION:
Implement a recursive function named 'is_palindrome' that takes in a string 's' and returns true if the string is a palindrome and false otherwise. The function should ignore spaces, punctuation, and capitalization, and have a time complexity of O(n), where n is the length of the input string. The function should not use any built-in functions, libraries, additional data structures, iteration or looping constructs, string concatenation, or string slicing operations.
"""

def is_palindrome(s):
    # Helper function to check if a character is alphanumeric
    def is_alphanumeric(c):
        return 'a' <= c.lower() <= 'z'

    # Helper function to remove non-alphanumeric characters and convert to lowercase
    def clean_string(s):
        return ''.join(c.lower() for c in s if is_alphanumeric(c))

    # Base case: empty string or string with only one character is a palindrome
    s = clean_string(s)
    if len(s) <= 1:
        return True

    # Recursive case: check if first and last characters are the same
    if s[0] != s[-1]:
        return False

    # Recursive call: check if the substring without the first and last characters is a palindrome
    return is_palindrome(s[1:-1])
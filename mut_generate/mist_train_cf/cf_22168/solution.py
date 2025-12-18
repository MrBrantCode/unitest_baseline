"""
QUESTION:
Implement a function named `is_palindrome` that takes a single string parameter and returns `True` if the string is a palindrome (ignoring spaces, punctuation, and capitalization) and `False` otherwise. The function should use only recursion (no loops or external loops), have a time complexity of O(n), and not use any built-in functions, libraries, or auxiliary variables to store intermediate results. The function should handle strings of any length, including empty strings and edge cases with only one character or multiple spaces and punctuation marks.
"""

def is_palindrome(string):
    # Define valid characters (letters) and their lowercase counterparts
    valid_chars = {chr(i): True for i in range(ord('a'), ord('z') + 1)}
    valid_chars.update({chr(i): True for i in range(ord('A'), ord('Z') + 1)})

    def is_palindrome_helper(string, left, right):
        # Base case: both pointers have crossed each other or are equal
        if left >= right:
            return True

        # Check if characters at current pointers are valid and equal
        if valid_chars.get(string[left], False) and valid_chars.get(string[right], False):
            if string[left].lower() != string[right].lower():
                return False
            else:
                # Recursively call the helper function with updated pointers
                return is_palindrome_helper(string, left + 1, right - 1)
        else:
            # Recursively call the helper function with updated pointers
            if not valid_chars.get(string[left], False):
                return is_palindrome_helper(string, left + 1, right)
            else:
                return is_palindrome_helper(string, left, right - 1)

    return is_palindrome_helper(string, 0, len(string) - 1)
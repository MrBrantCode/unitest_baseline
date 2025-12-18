"""
QUESTION:
Write a function `is_palindrome_recursive` that determines if an input string is a palindrome, considering both uppercase and lowercase letters, and ignoring any non-alphabetic characters. The function must have a time complexity of O(n), where n is the length of the input string. Do not use any built-in string manipulation functions, data structures, or loops in your recursive algorithm.
"""

def is_palindrome_recursive(s):
    # Helper function to check if a character is alphabetic
    def is_alphabetic(char):
        return 'a' <= char <= 'z' or 'A' <= char <= 'Z'

    # Recursive function to check if the string is a palindrome
    def check_palindrome(left, right):
        # Base case: if left and right are the same character or adjacent characters,
        # it means the string is a palindrome
        if left >= right:
            return True

        # Move the left index to the right until we find a valid alphabetic character
        while left < right and not is_alphabetic(s[left]):
            left += 1

        # Move the right index to the left until we find a valid alphabetic character
        while left < right and not is_alphabetic(s[right]):
            right -= 1

        # If the characters at the left and right indexes are not the same, the string is not a palindrome
        if s[left].lower() != s[right].lower():
            return False

        # Recurse with the updated indexes
        return check_palindrome(left + 1, right - 1)

    # Start the recursive function with the initial indexes
    return check_palindrome(0, len(s) - 1)
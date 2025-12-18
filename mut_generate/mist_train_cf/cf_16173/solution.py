"""
QUESTION:
Create a function named `create_palindrome` that takes a string of characters as input and returns a palindrome string. The function should only consider lowercase alphabets and ignore special characters and numbers. The function should have a time complexity of O(n^2) and should not use any additional data structures.
"""

def create_palindrome(s):
    """
    This function takes a string of characters as input and returns a palindrome string.
    It only considers lowercase alphabets and ignores special characters and numbers.
    
    Parameters:
    s (str): The input string
    
    Returns:
    str: A palindrome string
    """
    palindrome = ''
    for ch in s:
        if ch.isalpha():
            palindrome = ch.lower() + palindrome
    left, right = 0, len(palindrome) - 1
    while left < right:
        if palindrome[left] == palindrome[right]:
            left += 1
            right -= 1
        else:
            break
    if left >= right:
        return palindrome + palindrome[::-1]
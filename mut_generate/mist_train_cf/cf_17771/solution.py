"""
QUESTION:
Write a function `is_palindrome(string)` that takes a string of up to 10^6 characters as input and returns True if the string is a palindrome (reads the same backward as forward) and False otherwise. The function should have a time complexity of O(n), where n is the length of the string, and a space complexity of O(1). It should not use any built-in functions or libraries to check for palindromes.
"""

def entance(string):
    # initialize two pointers
    left = 0
    right = len(string) - 1

    # iterate until the pointers meet in the middle
    while left < right:
        # compare characters at left and right pointers
        if string[left] != string[right]:
            return False
        # move the pointers towards the middle
        left += 1
        right -= 1

    return True
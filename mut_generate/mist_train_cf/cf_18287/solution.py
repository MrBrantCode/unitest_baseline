"""
QUESTION:
Write a function `is_palindrome(lst)` that checks if a given list of elements is a palindrome, ignoring non-alphanumeric characters and treating uppercase and lowercase letters as the same character. The list can have a maximum length of 100 elements and the function should have a time complexity of O(n), where n is the length of the list.
"""

def is_palindrome(lst):
    clean_list = [str(x).lower() for x in lst if str(x).isalnum()]
    left = 0
    right = len(clean_list) - 1

    while left <= right:
        if clean_list[left] != clean_list[right]:
            return False
        left += 1
        right -= 1

    return True
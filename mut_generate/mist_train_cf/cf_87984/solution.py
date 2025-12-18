"""
QUESTION:
Write a function `is_palindrome` that takes a list `lst` of mixed elements as input, where the list can have a maximum length of 100 elements. The function should ignore non-alphanumeric characters, treat uppercase and lowercase letters as the same character, and return `True` if the list is a palindrome and `False` otherwise. The function should have a time complexity of O(n), where n is the length of the list.
"""

def is_palindrome(lst):
    start = 0
    end = len(lst) - 1

    while start < end:
        while start < end and not str(lst[start]).isalnum():
            start += 1
        while start < end and not str(lst[end]).isalnum():
            end -= 1

        if start >= end:
            break

        if str(lst[start]).lower() != str(lst[end]).lower():
            return False

        start += 1
        end -= 1

    return True
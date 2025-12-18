"""
QUESTION:
Write a function `is_palindrome` that takes a list of mixed elements as input and returns a boolean indicating whether the list is a palindrome. The function should ignore non-alphanumeric characters and treat uppercase and lowercase letters as the same character. The list can have a maximum length of 100 elements and the solution should have a time complexity of O(n), where n is the length of the list.
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
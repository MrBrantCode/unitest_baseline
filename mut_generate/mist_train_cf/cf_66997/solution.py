"""
QUESTION:
Write a function `make_palindrome(lst)` that takes a list `lst` as input and modifies it in-place to make it a palindrome, without creating a new list. The function should return the modified list. The input list is guaranteed to be non-empty.
"""

def make_palindrome(lst):
    lst += lst[-2::-1]
    return lst
"""
QUESTION:
Write a function named `check_second_letter` that takes a list of strings as its argument. This function should return `True` if at least one string in the list has 'e' as its second character (case sensitive), and `False` otherwise. The function should handle strings with less than 2 characters without raising an error.
"""

def check_second_letter(lst):
    for word in lst:
        if len(word) > 1 and word[1] == 'e':
            return True
    return False
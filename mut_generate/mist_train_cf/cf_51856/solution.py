"""
QUESTION:
Write a function `find_without_inverse` that takes a list of integers as input and returns a list of integers that do not have their inverse (i.e., their negation) in the input list.
"""

def find_without_inverse(lst):
    return [num for num in lst if -num not in lst]
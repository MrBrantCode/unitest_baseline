"""
QUESTION:
Write a function `contains_in_order` that takes an array of two alphanumeric strings as input. The function should return `True` if the characters in the second string appear consecutively and in the same order within the first string, and `False` otherwise.
"""

def contains_in_order(entities):
    s1, s2 = entities
    start = 0
    for ch in s2:
        i = s1.find(ch, start)
        if i == -1:
            return False
        start = i + 1
    return True
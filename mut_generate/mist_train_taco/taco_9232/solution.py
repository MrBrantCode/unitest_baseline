"""
QUESTION:
Write a function, that doubles every second integer in a list starting from the left.
"""

def double_every_other(l):
    return [x * 2 if i % 2 else x for (i, x) in enumerate(l)]
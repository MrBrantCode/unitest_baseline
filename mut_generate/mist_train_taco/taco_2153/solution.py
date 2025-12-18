"""
QUESTION:
Count how often sign changes in array.

### result
number from `0` to ... . Empty array returns `0`

### example
"""

def count_sign_changes(lst):
    count = 0
    for i in range(1, len(lst)):
        if (lst[i] < 0 and lst[i - 1] >= 0) or (lst[i] >= 0 and lst[i - 1] < 0):
            count += 1
    return count
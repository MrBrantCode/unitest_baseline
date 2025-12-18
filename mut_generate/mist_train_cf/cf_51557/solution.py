"""
QUESTION:
Create a function called `contains_ordered` that takes two alphanumeric strings as input, `sub` and `main`, and returns a boolean indicating whether all letters (case-insensitive) from `sub` are contained in the same order within `main`.
"""

def contains_ordered(sub, main):
    sub = sub.lower()
    main = main.lower()
    
    index = 0 
    for char in main:
        if index == len(sub):
            break
        if char == sub[index]:
            index += 1

    return index == len(sub)
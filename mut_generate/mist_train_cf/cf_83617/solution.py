"""
QUESTION:
Create a function named `count_sheeps` that takes a list of boolean values representing the presence or absence of sheep. The function should return the total number of sheep present (i.e., the number of True values in the list).
"""

def count_sheeps(sheep):
    total = 0
    for i in sheep:
        if i == True:
            total += 1
    return total
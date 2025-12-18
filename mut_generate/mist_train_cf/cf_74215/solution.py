"""
QUESTION:
Write a function `replace_last_three_fruits` that takes a list of strings and a string as input, and replaces the last three elements of the list with the given string. If the list has less than three elements, it should print "Not enough fruit to replace!" and return the original list.
"""

def replace_last_three_fruits(words, new_fruit):
    if len(words) >= 3:
        words[-3:] = [new_fruit]*3
    else:
        print("Not enough fruit to replace!")
    return words
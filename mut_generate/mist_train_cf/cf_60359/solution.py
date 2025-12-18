"""
QUESTION:
Implement a function `replace_cat_with_dog(s)` that takes a string `s` as input and replaces all occurrences of "cat" with "dog" without using any built-in string replace function/method. The function should achieve this in a space-efficient manner.
"""

def replace_cat_with_dog(s):
    i = 0
    output = ""
    while i < len(s):
        if s[i:i+3] == "cat":
            output += "dog"
            i += 3
        else:
            output += s[i]
            i += 1
    return output
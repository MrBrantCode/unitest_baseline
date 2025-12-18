"""
QUESTION:
Create a function named `alternate_case` that takes a string `s` as input and returns a new string with alternating case for each character (every even index character in upper case and every odd index character in lower case). Additionally, create a new list that reverses the order of the original list's elements and applies the `alternate_case` function to each string element without using built-in reverse functions.
"""

def alternate_case(s):
    return ''.join(c.upper() if i%2 == 0 else c.lower() for i, c in enumerate(s))

def reverse_and_apply(old_list):
    new_list = []
    for i in range(len(old_list)-1,-1,-1):
        new_list.append(alternate_case(old_list[i]))
    return new_list
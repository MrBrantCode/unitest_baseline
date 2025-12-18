"""
QUESTION:
Create a function `ascii_sort` that takes a string as input and returns a new string containing unique lowercase alphabets in ascending order of their ASCII values. The function should ignore any non-lowercase alphabet characters in the input string and not use any built-in sorting functions or data structures.
"""

def ascii_sort(string):
    lowercase_string = ""
    for char in string:
        if char.islower():
            lowercase_string += char

    unique_letters = ""
    for char in lowercase_string:
        if char not in unique_letters:
            unique_letters += char

    sorted_string = ""
    for i in range(97, 123): 
        for char in unique_letters:
            if ord(char) == i:
                sorted_string += char

    return sorted_string
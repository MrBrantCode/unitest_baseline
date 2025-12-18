"""
QUESTION:
Write a function named `reverse_and_remove_duplicates` that takes an input string as a parameter and returns the string in reverse order with no duplicate characters.
"""

def reverse_and_remove_duplicates(input_string):
    reversed_string = input_string[::-1]
    final_string = ""
    for char in reversed_string:
        if char not in final_string:
            final_string += char
    return final_string
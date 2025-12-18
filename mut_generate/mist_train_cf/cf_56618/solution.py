"""
QUESTION:
Create a function named `replace_and_count` that takes in a string `string` and two characters `find` and `replace`. The function should replace all occurrences of `find` with `replace` in the string, considering case sensitivity, and return a tuple containing the modified string and the count of replacements made.
"""

def replace_and_count(string, find, replace):
    response = ""
    counter = 0
    for element in string:
        if element == find:
            response += replace
            counter += 1
        else:
            response += element
    return response, counter
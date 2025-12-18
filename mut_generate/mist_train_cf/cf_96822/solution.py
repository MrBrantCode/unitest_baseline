"""
QUESTION:
Write a function `remove_occurrences(my_string, letter)` that takes a string `my_string` and a character `letter` as input, and returns a tuple containing the modified string with all occurrences of `letter` that are followed by a digit removed, and the count of occurrences removed. The function should also remove trailing spaces from the resulting string.
"""

def remove_occurrences(my_string, letter):
    occurrences_removed = 0
    i = 0

    while i < len(my_string):
        if my_string[i] == letter and i + 1 < len(my_string) and my_string[i+1].isdigit():
            my_string = my_string[:i] + my_string[i+1:]
            occurrences_removed += 1
        else:
            i += 1

    resulting_string = my_string.rstrip()

    return resulting_string, occurrences_removed
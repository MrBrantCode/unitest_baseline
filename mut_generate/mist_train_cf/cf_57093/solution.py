"""
QUESTION:
Create a function `capitalize_sentences` that takes two strings as input, capitalizes the initial letter of each sentence in the second string, and counts the number of differences between the modified second string and the first string. A sentence is defined to end at a period followed by a space. The function should not use any built-in/library string manipulation functions apart from `len` and `upper`.
"""

def capitalize_sentences(first_string, second_string):
    # Initialize variables
    modify_string, flag = "", True
    count_diff = 0

    # Loop through each character in the second string
    for i in range(len(second_string)):
        # If flag is true, capitalize the current character
        if flag and second_string[i] != ' ' and second_string[i] != '.':
            modify_string += second_string[i].upper()
            flag = False

        # If the current character is a period, check the next character
        elif second_string[i] == '.' and i + 1 < len(second_string) and second_string[i+1] == ' ':
            modify_string += second_string[i]
            flag = True

        # Just append the current character
        else:
            modify_string += second_string[i]

    # Compare the two strings
    for i in range(min(len(first_string), len(modify_string))):
        count_diff += first_string[i] != modify_string[i]

    # Add remaining characters
    count_diff += abs(len(first_string) - len(modify_string))

    return modify_string, count_diff
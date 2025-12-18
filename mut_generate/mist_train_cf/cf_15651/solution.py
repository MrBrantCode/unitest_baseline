"""
QUESTION:
Create a function named `count_lower_alphabets` that takes a string as input and returns the number of lowercase alphabets in the string, excluding any occurrences of the letters 'a' and 'b'. Implement this function using recursion and handle both lowercase and uppercase alphabets, as well as non-alphabet characters. The function should not modify the input string.
"""

def count_lower_alphabets(string):
    if string == "":
        return 0
    elif string[0].lower() in ['a', 'b']:
        return count_lower_alphabets(string[1:])
    elif string[0].islower():
        return 1 + count_lower_alphabets(string[1:])
    else:
        return count_lower_alphabets(string[1:])
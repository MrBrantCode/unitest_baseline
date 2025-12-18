"""
QUESTION:
Write a function named `count_lower_alphabets` that takes a string as input and returns the count of lowercase alphabets in the string, excluding the letters 'a' and 'b'. The function must use recursion and does not use any loops or built-in string or list methods that could simplify the problem.
"""

def count_lower_alphabets(string):
    if string == "":
        return 0
    elif string[0] in ['a', 'b']:
        return count_lower_alphabets(string[1:])
    elif string[0].islower():
        return 1 + count_lower_alphabets(string[1:])
    else:
        return count_lower_alphabets(string[1:])
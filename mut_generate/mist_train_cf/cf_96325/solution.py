"""
QUESTION:
Implement a function called `double_up` that takes a list of strings as input and returns a new list where each string in the input list is concatenated with itself. The function should also return the character at the index equal to the length of the input string minus one.
"""

def double_up(strings):
    return [(string + string)[len(string) - 1] for string in strings]
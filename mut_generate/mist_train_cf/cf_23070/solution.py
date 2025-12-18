"""
QUESTION:
Write a function `repeat_characters(string)` that takes a string as input and returns a string where each character of the input string is repeated five times, separated by a comma and a space. The function should have a time complexity of O(n), where n is the length of the input string.
"""

def repeat_characters(string):
    output = []
    for char in string:
        output.append((char + ", ") * 5)
    return "".join(output)[:-2]
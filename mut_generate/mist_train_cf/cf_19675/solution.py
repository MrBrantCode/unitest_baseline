"""
QUESTION:
Write a function `format_strings` that takes a list of strings as input and returns a list of strings where the first letter of each word in each string is capitalized. The function should have a time complexity of O(n) and a space complexity of O(1).
"""

def format_strings(strings):
    formatted_strings = []
    for string in strings:
        words = string.split(" ")
        formatted_words = [word.capitalize() for word in words]
        formatted_string = " ".join(formatted_words)
        formatted_strings.append(formatted_string)
    return formatted_strings
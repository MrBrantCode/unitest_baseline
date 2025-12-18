"""
QUESTION:
Write a function called `find_palindromes` that takes in a list of strings as input and returns a new list containing only the strings that are palindromes, ignoring spaces, punctuation, and capitalization. A palindrome is a word or phrase that reads the same backward as forward. The function should have a time complexity of O(n), where n is the length of the input list.
"""

def find_palindromes(strings):
    result = []
    for string in strings:
        lowercase_string = string.lower().replace(" ", "").replace(".", "").replace(",", "")
        if lowercase_string == lowercase_string[::-1]:
            result.append(string)
    return result
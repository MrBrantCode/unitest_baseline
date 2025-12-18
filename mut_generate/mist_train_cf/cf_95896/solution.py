"""
QUESTION:
Write a function `find_palindromes` that takes in a list of strings and returns a new list containing only the strings that are palindromes, ignoring spaces, punctuation, and capitalization. The function should have a time complexity of O(n), where n is the length of the input list. A palindrome is a word or phrase that reads the same backward as forward.
"""

def find_palindromes(strings):
    result = []
    for string in strings:
        lowercase_string = string.lower().replace(" ", "").replace(".", "").replace(",", "") 
        if lowercase_string == lowercase_string[::-1]: 
            result.append(string)
    return result
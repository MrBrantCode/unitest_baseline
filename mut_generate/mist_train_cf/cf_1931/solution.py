"""
QUESTION:
Write a function `retrieve_third_char` that takes a string as input. If the string length is greater than 10, all characters in the string are lowercase alphabetic, and the first two characters are both vowels, return the third character of the string. Otherwise, return a message indicating the retrieval was unsuccessful.
"""

def retrieve_third_char(s):
    if len(s) > 10 and s.isalpha() and s.islower() and s[0] in 'aeiou' and s[1] in 'aeiou':
        return s[2]
    else:
        return "Could not retrieve the third character."
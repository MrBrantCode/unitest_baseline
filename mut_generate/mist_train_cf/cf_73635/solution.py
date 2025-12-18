"""
QUESTION:
Write a function called `extract_lexemes` that takes an array of strings as input and returns a new list containing only the strings that have a length greater than 5 and meet an additional condition. The additional condition is assumed to be that the string contains only alphanumeric characters (letters and/or numbers).
"""

def extract_lexemes(arr):
    return [word for word in arr if len(word) > 5 and word.isalnum()]
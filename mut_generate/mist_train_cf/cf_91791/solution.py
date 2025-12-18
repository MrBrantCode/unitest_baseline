"""
QUESTION:
Implement a function named `search_keyword` that takes a dictionary and a keyword as input. The function should return a new dictionary containing all key-value pairs where the keyword is found either in the key itself or within any word in the value. Partial matches within the value are allowed, meaning the keyword does not need to be a complete word to be considered a match.
"""

def search_keyword(dictionary, keyword):
    result = {}
    for key, value in dictionary.items():
        if keyword in key or any(keyword in word for word in value.split()):
            result[key] = value
    return result
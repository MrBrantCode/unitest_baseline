"""
QUESTION:
Write a function `search_keyword` that takes a dictionary and a keyword as input and returns a new dictionary containing key-value pairs where the keyword is found either in the key or within the value (allowing for partial matches).
"""

def search_keyword(dictionary, keyword):
    result = {}
    for key, value in dictionary.items():
        if keyword in key or any(keyword in word for word in value.split()):
            result[key] = value
    return result
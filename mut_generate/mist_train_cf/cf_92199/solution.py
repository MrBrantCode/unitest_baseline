"""
QUESTION:
Write a function called `access_first_element` that takes a dictionary as input, where the dictionary contains a nested list. The function should return the first element of the nested list without modifying the list. The dictionary is in the format `{'list': [6, 7, 8]}`.
"""

def access_first_element(data):
    return data['list'][0]
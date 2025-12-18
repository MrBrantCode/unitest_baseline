"""
QUESTION:
Write a function `find_entries` that takes a list of dictionaries as input and returns a list of dictionaries where the value of the 'Name' key is 'John', the value of the 'Age' key is greater than 25, and the value of the 'Height' key is less than 180. The input list can have up to 10,000 dictionaries.
"""

def find_entries(list_of_dicts):
    return [dictionary for dictionary in list_of_dicts 
            if dictionary.get('Name') == 'John' and dictionary.get('Age') > 25 and dictionary.get('Height') < 180]
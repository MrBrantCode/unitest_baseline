"""
QUESTION:
Write a function `find_entries` that takes a list of dictionaries as input. The function should return a list of dictionaries where each dictionary has the key 'Name' with value 'John', the key 'Age' with a value greater than 25, and the key 'Height' with a value less than 180. The input list can have up to 10,000 entries.
"""

def find_entries(list_of_dicts):
    result = []
    for dictionary in list_of_dicts:
        if dictionary['Name'] == 'John' and dictionary['Age'] > 25 and dictionary['Height'] < 180:
            result.append(dictionary)
    return result
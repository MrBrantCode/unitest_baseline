"""
QUESTION:
Write a function `find_youngest_highest_id(response, nationality)` that takes a JSON string response and a nationality string as input. The function should parse the JSON response, which contains an array of objects, each with a unique id (integer), name (string), age (integer), and nationality (string). It should then find the name of the person who is both the youngest and has the highest id among those with the given nationality, and return this name as a string. If no person with the given nationality is found, the function should return `None`.
"""

import json

def find_youngest_highest_id(response, nationality):
    data = json.loads(response)
    youngest = None
    highest_id = None

    for obj in data:
        if obj['nationality'] == nationality:
            if youngest is None or obj['age'] < youngest['age']:
                youngest = obj
                highest_id = obj['id']
            elif obj['age'] == youngest['age'] and obj['id'] > highest_id:
                highest_id = obj['id']

    return youngest['name'] if youngest else None
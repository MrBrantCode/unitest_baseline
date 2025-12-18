"""
QUESTION:
Given a JSON array of objects, each containing 'id', 'name', 'age', and 'nationality', write a function `find_youngest_highest_id` that takes this JSON array and a specific nationality as input, and returns the name of the person who is both the youngest and has the highest 'id' among those with the given nationality. If no person with the given nationality is found, return `None`.
"""

def find_youngest_highest_id(response, nationality):
    import json
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
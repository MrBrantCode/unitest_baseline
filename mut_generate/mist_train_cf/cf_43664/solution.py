"""
QUESTION:
Write a function named `decode_and_restructure_json` to take a JSON string `json_string` as input and return the restructured JSON string. The function should decode the JSON string, calculate the average age of all people, and restructure the obtained information into a new JSON structure containing the average age and the education and occupational details of each person.
"""

import json
import statistics

def decode_and_restructure_json(json_string):
    data = json.loads(json_string)
    
    average_age = statistics.mean([person['age'] for person in data['people']])
    
    new_json = {"average_age": average_age, "people": []}
    
    for person in data['people']:
        new_person = {
            "name": person['name'],
            "education": person['details']['education'],
            "occupation": person['details']['occupation'],
        }
        new_json['people'].append(new_person)
        
    return json.dumps(new_json, indent=4)
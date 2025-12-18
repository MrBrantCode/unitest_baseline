"""
QUESTION:
Write a function named `process_data` that takes a list of dictionaries as an argument. Each dictionary represents a person and contains keys for 'first_name', 'last_name', 'email', and 'age'. The function must perform two transformations: 
1. Filter out people who are less than 18 years old.
2. Extract only the full name and email of the remaining people.

The function should return the transformed list of dictionaries.
"""

def process_data(info):
    # Phase 1: Filter minors.
    info = [person for person in info if person['age'] >= 18]

    # Phase 2: Extract only the name and email.
    info = [{'name': person['first_name'] + ' ' + person['last_name'], 'email': person['email']} for person in info]
 
    return info
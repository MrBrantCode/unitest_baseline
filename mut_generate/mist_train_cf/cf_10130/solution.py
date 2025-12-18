"""
QUESTION:
Create a function `preprocess_data` that takes a list of dictionaries as input, where each dictionary contains information about a person, including "name", "age", "gender", "city", and "hobbies". The function should return a modified list of dictionaries with the following changes:

- Replace "age" with "age_group" based on the following age ranges:
  - 0-10 years old: "child"
  - 11-18 years old: "teenager"
  - 19-30 years old: "young adult"
  - 31-50 years old: "adult"
  - 51 years old and above: "senior"
- Replace "city" with "location" based on the following city locations:
  - "New York": "East Coast"
  - "Los Angeles": "West Coast"
  - "Chicago": "Midwest"
  - "Houston": "South"
  - Other cities: "Other"

The input list can have any number of dictionaries, and the "hobbies" attribute can have any number of strings.
"""

def preprocess_data(data):
    for person in data:
        # Assign age group
        age = person['age']
        if age <= 10:
            person['age_group'] = 'child'
        elif age <= 18:
            person['age_group'] = 'teenager'
        elif age <= 30:
            person['age_group'] = 'young adult'
        elif age <= 50:
            person['age_group'] = 'adult'
        else:
            person['age_group'] = 'senior'
        
        # Assign location
        city = person['city']
        if city == 'New York':
            person['location'] = 'East Coast'
        elif city == 'Los Angeles':
            person['location'] = 'West Coast'
        elif city == 'Chicago':
            person['location'] = 'Midwest'
        elif city == 'Houston':
            person['location'] = 'South'
        else:
            person['location'] = 'Other'
    
    return data
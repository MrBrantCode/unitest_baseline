"""
QUESTION:
Create a function `count_males(json_data)` that takes a JSON list of people with 'name', 'age', and 'gender' attributes, and returns the number of males whose age is between 20 and 40 (inclusive).
"""

def count_males(json_data):
    count = 0
    for person in json_data:
        if person['gender'] == 'Male' and 20 <= person['age'] <= 40:
            count += 1
    return count
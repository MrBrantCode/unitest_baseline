"""
QUESTION:
Design a function named `get_average_age` that calculates the average age of people in a given JSON array. The JSON array contains objects representing people with "name" and "age" attributes. The function should parse the JSON array, iterate through each person, check for "name" and "age" attributes, calculate the average age, and return it. The average age should be rounded to two decimal places. The function should handle cases where the input JSON array is empty or contains people without "name" or "age" attributes.
"""

import json

def get_average_age(json_array):
    people = json.loads(json_array)
    
    sum_age = 0
    count = 0
    
    for person in people:
        if "name" in person and "age" in person:
            sum_age += person["age"]
            count += 1
    
    if count > 0:
        average_age = sum_age / count
        return round(average_age, 2)
    else:
        return 0.0
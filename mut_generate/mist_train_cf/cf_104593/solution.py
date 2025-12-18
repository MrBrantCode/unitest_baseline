"""
QUESTION:
Design a function named `get_average_age` that takes a JSON array of people as input, where each person is represented as a dictionary with "name" and "age" attributes. The function should return the average age of the people in the array, rounded to two decimal places. If the input array is empty or no person has both "name" and "age" attributes, the function should return 0.00.
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
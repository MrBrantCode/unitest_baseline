"""
QUESTION:
Design a function `get_average_age` that takes a JSON array of people objects as input, where each person object has "name", "age", and "gender" attributes. The function should return a tuple containing the average age of males and females separately. Assume the JSON array is a string and the age is a numeric value. The function should handle cases where there are no males or females in the input array.
"""

import json

def get_average_age(json_array):
    # Parse JSON array into a Python list of dictionaries
    people = json.loads(json_array)
    
    # Initialize sum and counter variables for males and females
    sum_male_age = 0
    count_male = 0
    sum_female_age = 0
    count_female = 0
    
    # Iterate through each dictionary in the list
    for person in people:
        # Check if the dictionary has all three attributes
        if "name" in person and "age" in person and "gender" in person:
            age = person["age"]
            gender = person["gender"]
            
            # Check the value of the "gender" attribute and update sum and counter variables accordingly
            if gender == "Male":
                sum_male_age += age
                count_male += 1
            elif gender == "Female":
                sum_female_age += age
                count_female += 1
    
    # Calculate the average age for males and females
    average_male_age = sum_male_age / count_male if count_male > 0 else 0
    average_female_age = sum_female_age / count_female if count_female > 0 else 0
    
    # Return a tuple containing the calculated average ages for males and females
    return (average_male_age, average_female_age)
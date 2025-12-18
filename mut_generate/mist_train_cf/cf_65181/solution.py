"""
QUESTION:
Write a function named `get_stats` that calculates the average age of females and males in a given list of JSON data. The function should filter out any invalid entries, such as those missing 'age' or 'gender' fields, or those with non-numeric or negative 'age' values. The function should handle edge cases where there are no valid female or male entries in the dataset. The function should return a dictionary containing the average age of females, average age of males, total count of valid female entries, and total count of valid male entries. If there are no valid entries for either gender, the corresponding average age should be returned as `None`. The function should also log any errors encountered during execution.
"""

import json

def get_stats(data):
    male_count = 0
    female_count = 0
    male_age = 0
    female_age = 0

    for d in data:
        try:
            if 'gender' not in d or 'age' not in d:
                raise Exception(f"Either Age or Gender missing : {d}")
            gender = d['gender']
            if type(gender) != str:
                raise Exception(f"Invalid gender : {gender}")
            age = d['age']
            if type(age) != int or age < 0:
                raise Exception(f"Invalid age : {age}")
            if gender.lower() == "male":
                male_age += age
                male_count += 1
            elif gender.lower() == "female":
                female_age += age
                female_count += 1
        except Exception as e:
            print(f"Invalid data entry : {e}")
    return {'male_avg_age': male_age / male_count if male_count > 0 else None,
           'female_avg_age': female_age / female_count if female_count > 0 else None,
           'male_count' : male_count,
           'female_count' : female_count}
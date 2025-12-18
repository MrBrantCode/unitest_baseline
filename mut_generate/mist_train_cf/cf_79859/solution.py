"""
QUESTION:
Write a function `calculate_average_age` that takes in a list of JSON objects, a specific `gender`, and a specific `nationality`. The function should calculate the average age of individuals matching the specified `gender` and `nationality`, skipping any records with missing or inconsistent data. If no matching records are found, the function should return a message indicating so. The function should be case-insensitive when comparing `gender` and `nationality`.
"""

def calculate_average_age(data, gender, nationality):
    total_age = 0
    count = 0
    for record in data:
        try:
            # checking if the record matches our criteria
            if record['gender'].lower() == gender.lower() and record['nationality'].lower() == nationality.lower():
                # if age is not a number, it will raise a ValueError
                total_age += int(record['age'])
                count += 1
        except (KeyError, ValueError):
            # If there is a KeyError (missing data) or ValueError (inconsistency), 
            # just skip the record and continue with the next record
            continue
    
    # handling case when there is no matching record
    if count == 0:
        return "No matching record found"

    return total_age / count
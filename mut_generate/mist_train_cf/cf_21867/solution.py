"""
QUESTION:
Create a function `count_males` that takes JSON data as input and returns the number of males in the dataset, ignoring individuals whose age is less than 20 or greater than 40. The function should have a time complexity of O(n), where n is the number of individuals in the dataset. The JSON data is assumed to be a list of objects, each containing 'age' and 'gender' keys.
"""

def count_males(json_data):
    count = 0
    individuals = json.loads(json_data)

    for individual in individuals:
        age = individual['age']
        if 20 <= age <= 40 and individual['gender'] == 'male':
            count += 1

    return count
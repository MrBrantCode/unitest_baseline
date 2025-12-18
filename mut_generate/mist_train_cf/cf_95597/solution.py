"""
QUESTION:
Write a function `convert_to_tuple_of_tuples` that takes a list of dictionaries as input, where each dictionary represents a person with 'name' and 'age' keys. The function should return a tuple of tuples, where each inner tuple contains the person's name capitalized and age as a positive integer. If a person's name or age is missing or invalid, skip that dictionary. The resulting tuple of tuples should be sorted in descending order based on the person's age.
"""

def convert_to_tuple_of_tuples(persons):
    valid_persons = [(person['name'].capitalize(), person['age']) for person in persons
                     if 'name' in person and isinstance(person['name'], str)
                     and 'age' in person and isinstance(person['age'], int) and person['age'] > 0]

    sorted_persons = sorted(valid_persons, key=lambda x: x[1], reverse=True)

    return tuple(sorted_persons)
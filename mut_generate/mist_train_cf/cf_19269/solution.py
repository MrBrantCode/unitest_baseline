"""
QUESTION:
Write a function named `convert_to_tuple_of_tuples` that takes a list of dictionaries as input. Each dictionary is expected to contain 'name' and 'age' keys. The function should filter out dictionaries with missing or invalid 'name' (non-string) or 'age' (non-positive integer), capitalize the 'name' values, and return a tuple of tuples containing the capitalized 'name' and 'age' of each valid person, sorted in descending order by 'age'.
"""

def convert_to_tuple_of_tuples(persons):
    valid_persons = [(person['name'].capitalize(), person['age']) for person in persons
                     if 'name' in person and isinstance(person['name'], str)
                     and 'age' in person and isinstance(person['age'], int) and person['age'] > 0]

    sorted_persons = sorted(valid_persons, key=lambda x: x[1], reverse=True)

    return tuple(sorted_persons)
"""
QUESTION:
Implement a `search` function to find individuals based on one or more criteria from a list of people. Each person is represented as a dictionary containing 'name', 'age', 'weight', and 'address', where 'address' is another dictionary with 'street', 'city', 'country', and 'postal_code'. The function should be able to search by any of these criteria and return a list of matching individuals.
"""

def search(people, criteria, value):
    results = []
    for person in people:
        if criteria in person:
            if person[criteria] == value:
                results.append(person)
        elif 'address' in person and criteria in person['address']:
            if person['address'][criteria] == value:
                results.append(person)
    return results
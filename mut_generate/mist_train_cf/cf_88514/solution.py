"""
QUESTION:
Create a function `sort_persons_list(persons)` that takes a list of dictionaries as input, where each dictionary represents a person with 'name' and 'age' keys. The function should return a tuple of tuples, where each inner tuple contains the capitalized name and the positive integer age of a person, sorted in descending order by age. The function should skip any dictionary that has a missing or invalid name or age. The implementation should have a time complexity of O(n^2) and a space complexity of O(n), where n is the number of valid dictionaries in the input list.
"""

def sort_persons_list(persons):
    valid_persons = []

    # Iterate over each dictionary in the given list
    for person in persons:
        name = person.get('name')
        age = person.get('age')

        # Check if the dictionary has a valid name and age
        if name and isinstance(name, str) and age and isinstance(age, int) and age > 0:
            # Capitalize the name
            name = name.capitalize()
            # Append the valid tuple to the list
            valid_persons.append((name, age))

    # Bubble sort the list of tuples in descending order based on the age
    n = len(valid_persons)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if valid_persons[j][1] < valid_persons[j + 1][1]:
                valid_persons[j], valid_persons[j + 1] = valid_persons[j + 1], valid_persons[j]

    # Return the sorted list of tuples as a tuple
    return tuple(valid_persons)
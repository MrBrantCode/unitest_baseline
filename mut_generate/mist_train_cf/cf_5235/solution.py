"""
QUESTION:
Implement a function called `process_people` that takes in a list of tuples, where each tuple represents a person's information containing the person's name (a string), age (an integer), and height (a float). 

The function should remove any tuples that have a duplicate name, filter out any tuples where the age is less than 18 or the height is less than 150, sort the modified list in descending order based on the length of the tuples, and return the modified list along with the average age and average height of the remaining tuples as a tuple.
"""

def process_people(people):
    # Remove tuples with duplicate names
    unique_people = []
    seen_names = set()
    for person in people:
        name = person[0]
        if name not in seen_names:
            unique_people.append(person)
            seen_names.add(name)

    # Filter out tuples with age less than 18 or height less than 150
    filtered_people = []
    for person in unique_people:
        age = person[1]
        height = person[2]
        if age >= 18 and height >= 150:
            filtered_people.append(person)

    # Sort the modified list in descending order based on tuple length
    sorted_people = sorted(filtered_people, key=lambda x: len(x), reverse=True)

    # Calculate average age and average height
    total_age = 0
    total_height = 0
    for person in sorted_people:
        total_age += person[1]
        total_height += person[2]
    avg_age = total_age / len(sorted_people)
    avg_height = total_height / len(sorted_people)

    return sorted_people, (avg_age, avg_height)
"""
QUESTION:
Write a function `print_people_info` that takes a list of dictionaries as input, where each dictionary contains 'name' and 'age' keys representing a person. The function should print each person's name followed by their age. Handle cases where the input list is empty or if any dictionary is missing the 'name' or 'age' keys by displaying an error message.
"""

def print_people_info(people):
    if not people:
        print("No people data available.")
        return

    for person in people:
        if 'name' not in person or 'age' not in person:
            print("Invalid person data:", person)
        else:
            print(person['name'], "is", person['age'], "years old.")
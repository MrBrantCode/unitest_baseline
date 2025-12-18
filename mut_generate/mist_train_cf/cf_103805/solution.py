"""
QUESTION:
Write a function `findOldestPerson` that takes a list of dictionaries representing people with 'name' and 'age' as keys, and returns the name and age of the oldest person. The age should be rounded to the nearest integer. The function should be able to handle a list of any length.
"""

def findOldestPerson(people):
    # Initialize variables to store the name and age of the oldest person
    oldest_name = ''
    oldest_age = 0
    
    # Iterate through each person in the list
    for person in people:
        # Get the rounded age of the person
        rounded_age = round(person['age'])
        
        # Check if the current person's age is greater than the oldest age found so far
        if rounded_age > oldest_age:
            oldest_name = person['name']
            oldest_age = rounded_age
            
    return oldest_name, oldest_age
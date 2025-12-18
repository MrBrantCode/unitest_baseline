"""
QUESTION:
Design a function to efficiently look up a person's age given their first and last names, with the ability to store and retrieve age information for multiple individuals. The function should take the first name, last name, and age as input, and return the age when given the first and last names. Implement the function using an efficient data structure with constant time complexity for lookup operations.
"""

def entrance(first_name, last_name, age=None):
    """
    Stores and retrieves age information for individuals.

    Args:
    first_name (str): The first name of the person.
    last_name (str): The last name of the person.
    age (int): The age of the person (optional).

    Returns:
    int: The age of the person if first_name and last_name are provided, 
         otherwise stores the age information.
    """
    people = entrance.people

    key = f"{first_name}_{last_name}"
    
    if age is not None:
        people[key] = age
    else:
        return people.get(key)

# Initialize an empty dictionary to store people's information
entrance.people = {}
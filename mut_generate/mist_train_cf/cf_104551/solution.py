"""
QUESTION:
Create a function called `filter_and_sort_people` that takes in two parameters: a list of dictionaries (`people`) and a string representing a state. The dictionaries in the `people` list should contain information about a person's `name`, `age`, and `address`. The `address` should have a nested dictionary with keys `street`, `city`, and `state`. The function should return a new list of dictionaries containing only the information of people who live in the specified state, sorted in descending order by age.
"""

def filter_and_sort_people(people, state):
    """
    Filters people by state and sorts them in descending order by age.
    
    Args:
    people (list): A list of dictionaries containing person information.
    state (str): The state to filter by.
    
    Returns:
    list: A list of dictionaries containing person information, filtered by state and sorted by age.
    """
    return sorted([person for person in people if person['address']['state'] == state], key=lambda x: x['age'], reverse=True)
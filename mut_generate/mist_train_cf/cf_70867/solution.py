"""
QUESTION:
Create a function `expunge_entity` that takes two parameters: a list `data` of indefinite length and an `entity`. The function should return a new list that excludes every instance of the `entity` from `data` without modifying the original list.
"""

def expunge_entity(data, entity):
    # Use list comprehension to create a new list that excludes the entity
    return [x for x in data if x != entity]
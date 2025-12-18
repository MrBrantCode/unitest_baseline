"""
QUESTION:
Create a function called 'filter_objects' that takes an array of objects as input. Each object is expected to have 'name' and 'date' attributes. The function should return a list of dictionaries containing 'name' and 'date' fields, but only for objects where the name starts with the letter "J" and the date is in the year 20.
"""

from datetime import datetime

def filter_objects(objects):
    """
    Filters a list of objects to include only those where the name starts with "J" and the date is in the year 2020.
    
    Args:
        objects (list): A list of objects with 'name' and 'date' attributes.
    
    Returns:
        list: A list of dictionaries containing 'name' and 'date' fields for the filtered objects.
    """
    
    return [
        {"name": obj.name, "date": obj.date}
        for obj in objects 
        if obj.name.startswith("J") and obj.date.year == 2020
    ]
"""
QUESTION:
Create a function `assign_category` that takes an object as input and returns 'living' if the object is 'dog', 'cat', or 'bird', and 'non-living' otherwise. Use this function to classify a given list of objects into two categories, 'living' and 'non-living', and store the classification in a dictionary. The given list of objects is ['dog', 'cat', 'tree', 'bird'].
"""

def assign_category(object):
    living_things = ['dog', 'cat', 'bird']
    if object in living_things:
        return 'living'
    else:
        return 'non-living'
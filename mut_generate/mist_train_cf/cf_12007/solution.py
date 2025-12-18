"""
QUESTION:
Convert the given list of dictionaries to a tuple of tuples using the function `convert_to_tuple`. Each inner tuple should contain the name and age of a person, with the name capitalized and the age as a positive integer. If a dictionary is missing a name or age, or if the name is not a string or the age is not a positive integer, skip that dictionary.
"""

def convert_to_tuple(lst):
    result = []
    for d in lst:
        name = d.get("name")
        age = d.get("age")
        if name and isinstance(name, str):
            name = name.capitalize()
        else:
            continue
        if age and isinstance(age, int) and age > 0:
            result.append((name, age))
    return tuple(result)
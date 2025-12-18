"""
QUESTION:
Sort the given array of objects based on the following criteria:
- In descending order of age
- For objects with the same age, in alphabetical order of name
- For objects with the same name, in ascending order of position

The array contains objects with 'name', 'age', and 'position' as keys. Write a function to sort the array according to the specified criteria.
"""

def sort_array_of_objects(data):
    return sorted(data, key=lambda x: (-x['age'], x['name'], x['position']))
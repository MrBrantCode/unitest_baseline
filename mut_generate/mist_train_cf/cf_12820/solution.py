"""
QUESTION:
Create a function named `compare_objects` that compares two objects with `name`, `age`, and `address` attributes. The function should return an integer value based on the following rules:
- If the ages of the two objects are different, return the difference in age.
- If the ages are the same, compare the names alphabetically and return the result of the comparison.
- If the names are also the same, compare the addresses alphabetically and return the result of the comparison.
- If all three attributes are the same, return 0.
"""

def compare_objects(obj1, obj2):
    if obj1.age != obj2.age:
        return obj1.age - obj2.age
    elif obj1.name != obj2.name:
        if obj1.name < obj2.name:
            return -1
        else:
            return 1
    else:
        if obj1.address < obj2.address:
            return -1
        elif obj1.address > obj2.address:
            return 1
        else:
            return 0
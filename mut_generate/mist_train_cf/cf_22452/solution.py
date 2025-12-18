"""
QUESTION:
Create a `__init__` method for a `Person` class to initialize an object with `name` (string), `age` (integer), and `hobbies` (list). The method should also create a unique identifier by combining the first letter of the `name` with the last two digits of the `age`. The identifier should be stored in the `identifier` attribute.
"""

def entrance(name, age, hobbies):
    return {"name": name, "age": age, "hobbies": hobbies, "identifier": name[0] + str(age)[-2:]}
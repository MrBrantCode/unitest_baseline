"""
QUESTION:
Implement the `areSimilar` function that compares two `Member` objects and determines if they are similar based on their schema properties and values. The function takes two `Member` objects as input and returns `True` if they have the same schema properties and corresponding values, and `False` otherwise. Assume the `Member` class has the following methods: `getSchemaProperties()` to return an array of schema properties for the member, and `getValue(property)` to return the value of the specified property for the member.
"""

def areSimilar(member1, member2):
    if member1.getSchemaProperties() != member2.getSchemaProperties():
        return False

    for property in member1.getSchemaProperties():
        if member1.getValue(property) != member2.getValue(property):
            return False

    return True
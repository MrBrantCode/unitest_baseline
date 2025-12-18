"""
QUESTION:
Write a function named `compare_by_age_descending` that sorts a list of objects (class `Person` with attributes `name`, `age`, `height`) in descending order based on their `age`. The function should be used as a key for the `sort()` method and should not modify the original list. Implement the `compare_by_age_descending` function and sort the list of `Person` objects. 

Note: The input list of `Person` objects is already defined. The `Person` class and the list of `Person` objects are already implemented.
"""

def compare_by_age_descending(person):
    return -person.age
"""
QUESTION:
Write a function named `compare_strings` that takes two string parameters, `Entity1` and `Entity2`. The function should compare the two strings in a case-insensitive manner and return the string that precedes the other alphabetically. If the strings are identical, the function should return "Equal". The function should handle edge cases such as mixed-case text strings and empty strings.
"""

def compare_strings(Entity1, Entity2):
    Entity1 = Entity1.lower()
    Entity2 = Entity2.lower()

    if Entity1 == Entity2:
        return "Equal"
    elif Entity1 > Entity2:
        return Entity2
    else:
        return Entity1
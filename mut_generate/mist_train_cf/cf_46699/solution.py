"""
QUESTION:
Write a function `remove_names(names)` that takes a list of names as input and returns a new list containing only the names that end with a consonant, preserving the original order and supporting different case inputs. The implementation should not use any in-built functions except those related to string and list manipulation.
"""

def remove_names(names):
    vowels = 'aeiou'
    filtered_names = []

    for name in names:
        last_char = name[-1].lower()
        if last_char not in vowels:
            filtered_names.append(name)

    return filtered_names
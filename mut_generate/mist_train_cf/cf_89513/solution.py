"""
QUESTION:
Create a function named `find_unique_names(names)` that takes a list of names as input and returns a set containing only the names with a length greater than 6 and no repeating characters. The solution must only use basic data structures such as lists and arrays, and must not use advanced data structures like sets or hash maps. If no such names exist, the function should return an empty set.
"""

def find_unique_names(names):
    unique_names = []
    for name in names:
        if len(name) > 6:
            is_unique = True
            for i in range(len(name)):
                for j in range(i + 1, len(name)):
                    if name[i] == name[j]:
                        is_unique = False
                        break
                if not is_unique:
                    break
            if is_unique:
                unique_names.append(name)
    return unique_names
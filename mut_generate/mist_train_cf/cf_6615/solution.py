"""
QUESTION:
Create a function called `find_unique_names` that takes a list of names as input and returns a set of names with length greater than 6 and no repeating characters. Use only basic data structures (arrays, linked lists, etc.) and do not use advanced data structures such as hash maps or sets. If no such names exist, return an empty set.
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
    return set(unique_names)
"""
QUESTION:
Create a function named `most_common_name` that takes a list of names as input and returns the name(s) that occur most frequently in the list. If there is a single most frequent name, return it. If there is a tie for the most frequent name, return a list of these names in alphabetical order. However, if the list is empty, contains only one name, or there is a tie for the most frequent name in a list with a single element, return an empty list.
"""

def entrance(names):
    if len(names) == 0 or len(names) == 1:
        return []

    name_counts = {}
    max_count = 0

    for name in names:
        if name in name_counts:
            name_counts[name] += 1
        else:
            name_counts[name] = 1

        if name_counts[name] > max_count:
            max_count = name_counts[name]

    most_common_names = []
    for name in name_counts:
        if name_counts[name] == max_count:
            most_common_names.append(name)

    if len(most_common_names) > 1:
        return sorted(most_common_names)
    else:
        return most_common_names[0]
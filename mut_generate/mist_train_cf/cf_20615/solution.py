"""
QUESTION:
Create a function named `sort_dictionary_by_length` that takes a dictionary of names and ages as input. The function should return a dictionary sorted by the sum of the length of the names and ages in descending order. If two or more people have the same sum of lengths, they should be sorted alphabetically by name in ascending order.
"""

def sort_dictionary_by_length(dictionary):
    # Create a list of tuples with name and age
    tuples = [(name, age) for name, age in dictionary.items()]

    # Sort the list of tuples
    sorted_tuples = sorted(tuples, key=lambda x: (-len(x[0]) - len(str(x[1])), x[0]), reverse=False)

    # Convert the sorted list of tuples back into a dictionary
    sorted_dict = {name: age for name, age in sorted_tuples}

    return sorted_dict
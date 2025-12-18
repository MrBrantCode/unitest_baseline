"""
QUESTION:
Create a function named `find_most_frequent_name` that takes a list of names as input, where each name can be any combination of uppercase and lowercase letters. The function should return the most frequent name in the list, treating names as case-insensitive. The time complexity of the solution should be O(n), where n is the number of names in the list.
"""

def find_most_frequent_name(names):
    # Create an empty dictionary
    frequency = {}

    # Initialize max_count and most_frequent_name
    max_count = 0
    most_frequent_name = ""

    # Iterate over each name in the array
    for name in names:
        # Convert the name to lowercase
        lowercase_name = name.lower()

        # If the lowercase name is already in the dictionary, increment its count by 1
        if lowercase_name in frequency:
            frequency[lowercase_name] += 1
        # Otherwise, add it to the dictionary with a count of 1
        else:
            frequency[lowercase_name] = 1

        # Update max_count and most_frequent_name if necessary
        if frequency[lowercase_name] > max_count:
            max_count = frequency[lowercase_name]
            most_frequent_name = lowercase_name

    # Return the most frequent name
    return most_frequent_name
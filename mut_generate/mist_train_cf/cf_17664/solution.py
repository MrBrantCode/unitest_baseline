"""
QUESTION:
Write a function `find_most_frequent_name` that takes an array of names as input and returns the most frequent name in a case-insensitive manner. The function should be able to handle an array of up to 10^6 names and should have a time complexity of O(n), where n is the number of names in the array.
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
"""
QUESTION:
Write a function named `count_unique_elements` that takes a list of tuples as input, where each tuple contains a string and a number. The function should return a dictionary where the keys are the unique strings in a case-insensitive manner and the values are the sum of the numbers associated with each unique string.
"""

def count_unique_elements(data_collection):
    # Convert all keys to lower-case for case insensitivity
    data_collection = [(item[0].lower(), item[1]) for item in data_collection]
    
    # Initializing an empty dictionary
    dist_elements_count = {}
    
    # Extract unique elements and count their repetitions
    for element, value in data_collection:
        # If the element is not in the dictionary, add it with its count
        if element not in dist_elements_count:
            dist_elements_count[element] = value
        # If the element is already in the dictionary, increment its count
        else:
            dist_elements_count[element] += value
    
    return dist_elements_count
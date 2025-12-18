"""
QUESTION:
Write a function `get_unique_data` that takes a list of tuples, where each tuple contains a string and an integer. The function should return a list of tuples containing only distinct elements based on both the strings and the integers. Any tuple containing a string or integer that appears more than once in the input list should be removed.
"""

def get_unique_data(data_collection):
    str_counts = {}
    num_counts = {}
    
    # Counting strings and integers
    for data in data_collection:
        str_counts[data[0]] = str_counts.get(data[0], 0) + 1
        num_counts[data[1]] = num_counts.get(data[1], 0) + 1
    
    # Filtering tuples which have unique string and integer
    unique_data = [data for data in data_collection if str_counts[data[0]] == 1 and num_counts[data[1]] == 1]
    
    return unique_data
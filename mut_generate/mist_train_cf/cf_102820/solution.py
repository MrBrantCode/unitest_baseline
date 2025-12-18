"""
QUESTION:
Create a function called "convert_to_dict" that takes a list of integers as input. The function should return a dictionary where the unique integers from the list are keys, and their corresponding values are the squares of the keys.
"""

def convert_to_dict(lst):
    result_dict = {}
    unique_set = set(lst)
    
    for item in unique_set:
        result_dict[item] = item ** 2
        
    return result_dict
"""
QUESTION:
Create a function named `sum_name_length` that calculates the cumulative length of a given list of names after removing names that start with a lowercase letter and names that contain non-alphabetical symbols. The function should handle potential edge cases where the list might be empty.
"""

def sum_name_length(names):
    filtered_names = [name for name in names if name[0].isupper() 
                    and name.isalpha()]
    total_length = 0 
    for name in filtered_names:
        total_length += len(name)
    return total_length
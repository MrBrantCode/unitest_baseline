"""
QUESTION:
Design a function named 'remove_duplicates' that takes a list as input and returns a new list with consecutive duplicate elements removed.
"""

def remove_duplicates(input_list):
    # Initializing an empty list to store the result
    result = []
  
    for item in input_list:
        if len(result) == 0 or item != result[-1]:
            result.append(item)
    return result
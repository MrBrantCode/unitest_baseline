"""
QUESTION:
Create a function called `remove_duplicates` that takes a list `lst` as input, removes duplicates while preserving the original order, and returns the resulting list. The list may contain integers, floats, strings, or a combination of these data types. The solution should have a time complexity of O(n), where n is the length of the input list.
"""

def remove_duplicates(lst):
    # Create an empty dictionary
    seen = {}
    
    # Create an empty list to store the unique elements
    result = []
    
    # Iterate over each element in the input list
    for item in lst:
        # Check if the element is already in the dictionary
        if item not in seen:
            # If not, add it to the dictionary and the result list
            seen[item] = True
            result.append(item)
    
    return result
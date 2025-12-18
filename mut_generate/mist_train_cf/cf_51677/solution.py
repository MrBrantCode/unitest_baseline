"""
QUESTION:
Create a function named `three_set_intersection` that takes three sets `s1`, `s2`, and `s3` as input. The function should return a list of elements that are common to all three sets, without any repetitions, and in numerical order. The function cannot use Python's built-in set operations.
"""

def three_set_intersection(s1: set, s2: set, s3: set):
    # Create an empty list to hold common elements
    common = []
    
    # Use a nested loop to find common elements
    for elem in s1:
        if elem in s2 and elem in s3:
            # Avoiding repetitions
            if elem not in common:
                common.append(elem)
                
    # Sort the list before returning
    common.sort()
    
    return common
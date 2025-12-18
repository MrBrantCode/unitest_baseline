"""
QUESTION:
Design a function named `is_subset(group1, group2)` that checks if all elements in `group1` are a subset of `group2` without repetition. The check should be case-insensitive and ignore white spaces in both groups. The function should return `True` if all elements in `group1` can be found in `group2` regardless of their case and white space arrangement, and `False` otherwise.
"""

def entance(group1, group2):
    # Initialize a subset checker
    subset_check = True

    # For each element in group1
    for i in group1:

        # Clean up the element by making it lower case and removing leading/trailing whitespaces
        cleaned_i = i.lower().strip()

        # Initialize a match checker
        match_check = False

        # For each element in group2
        for j in group2:

            # Clean up the element by making it lower case and removing all whitespaces
            cleaned_j = j.lower().replace(" ", "")

            # Check if the cleaned value in group1 is in cleaned group2
            if cleaned_i in cleaned_j:
                
                # If yes, this element from group1 is a match in group2
                match_check = True
                break
        
        # If there was no match for the particular group1 element, update subset checker to False
        if match_check is False:
            subset_check = False
            break

    # Return final subset checker
    return subset_check
"""
QUESTION:
Write a function `combine_unique_elements` that takes two lists as input, removes duplicates within each list, combines the unique elements from both lists into a new list, and returns the resulting list. The function should not maintain the original order of elements from the input lists.
"""

def combine_unique_elements(list1, list2):
    # Remove duplicates from list1
    list1 = list(set(list1))
    
    # Remove duplicates from list2
    list2 = list(set(list2))
    
    # Combine the unique elements from both lists
    combined_list = list1 + list2
    
    # Remove duplicates from the combined list
    combined_list = list(set(combined_list))
    
    # Convert the combined list back to a regular list
    combined_list = list(combined_list)
    
    # Return the combined list
    return combined_list
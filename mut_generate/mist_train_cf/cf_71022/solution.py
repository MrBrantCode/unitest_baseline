"""
QUESTION:
Write a function `calculate_disparity(list1, list2)` that calculates the frequency of elements unique to each list. The function should return a dictionary where the keys are the unique elements and the values are their frequencies. The function should handle cases where the lists are empty or contain non-integer elements.
"""

def calculate_disparity(list1, list2):
    # Create a set from each list
    set1 = set(list1)
    set2 = set(list2)
    
    # Calculate the symmetric difference (unique elements in both sets)
    unique_elements = set1.symmetric_difference(set2)
    
    # Calculate the frequency of unique elements
    frequency_dict = {}
    
    # First loop through list1 and count the frequency of elements
    for element in list1:
        if element in unique_elements:
            if element in frequency_dict:
                frequency_dict[element] += 1
            else:
                frequency_dict[element] = 1
                
    # Next, loop through list2 and count the frequency of elements
    for element in list2:
        if element in unique_elements:
            if element in frequency_dict:
                frequency_dict[element] += 1
            else:
                frequency_dict[element] = 1
                
    return frequency_dict
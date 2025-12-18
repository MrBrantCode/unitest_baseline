"""
QUESTION:
Write a function named `covariance` that calculates the covariance between two given lists. The lists may contain missing values represented by `None` and the lengths of the two lists may not be the same. The function should return `None` if either list is empty or contains only missing values.
"""

def covariance(list1, list2):
    # Check if both lists are empty or contain only missing values
    if (not list1 or all(value is None for value in list1)) and (not list2 or all(value is None for value in list2)):
        return None
    
    # Check if any of the lists is empty or contains only missing values
    if not list1 or all(value is None for value in list1) or not list2 or all(value is None for value in list2):
        return None
    
    # Remove missing values from both lists
    list1_filtered = [value for value in list1 if value is not None]
    list2_filtered = [value for value in list2 if value is not None]
    
    # Check if both filtered lists are empty
    if not list1_filtered or not list2_filtered:
        return None
    
    # Check if the lengths of the filtered lists are the same
    if len(list1_filtered) != len(list2_filtered):
        return None
    
    # Calculate the covariance
    mean1 = sum(list1_filtered) / len(list1_filtered)
    mean2 = sum(list2_filtered) / len(list2_filtered)
    
    covariance = sum((x - mean1) * (y - mean2) for x, y in zip(list1_filtered, list2_filtered)) / len(list1_filtered)
    return covariance
"""
QUESTION:
Write a function `find_common_fruits(fruits, citrus_fruits)` that takes two lists of fruits as input and returns the common fruits in alphabetical order, total count of items in each list, and the percentage of common items compared to the total number of items in both lists combined. The function should use Python programming language and assume that the input lists contain only strings.
"""

def find_common_fruits(fruits, citrus_fruits):
    # Find the items that are in both lists
    common_fruits = sorted(list(set(fruits) & set(citrus_fruits)))
    
    # Get the total count of items in each list
    total_fruits = len(fruits)
    total_citrus_fruits = len(citrus_fruits)
    
    # Get the count and percentage of items in the intersection
    common_count = len(common_fruits)
    common_percentage = (common_count / (total_fruits + total_citrus_fruits)) * 100
    
    return common_fruits, total_fruits, total_citrus_fruits, common_count, common_percentage
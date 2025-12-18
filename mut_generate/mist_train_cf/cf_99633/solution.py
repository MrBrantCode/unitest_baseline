"""
QUESTION:
Write a function `find_common_fruits` that takes two lists `fruits` and `citrus_fruits` as input. The function should find the common elements between the two lists, sort them alphabetically, and return the common elements along with the total count of elements in each list and the percentage of common elements compared to the total count of elements in both lists. The lists may contain duplicate elements.
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
    
    # Return the results
    return common_fruits, total_fruits, total_citrus_fruits, common_count, common_percentage
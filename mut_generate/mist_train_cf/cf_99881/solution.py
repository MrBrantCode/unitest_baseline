"""
QUESTION:
Write a function named `find_common_fruits` that takes two lists, `fruits` and `citrus_fruits`, as input and returns the common items between the two lists in alphabetical order, along with the count of items in each list and the percentage of common items compared to the total count of items in both lists.
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
    return {
        "Common fruits": common_fruits,
        "Total fruits": total_fruits,
        "Total citrus fruits": total_citrus_fruits,
        "Common count": common_count,
        "Common percentage": common_percentage
    }
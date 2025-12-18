"""
QUESTION:
Write a function `find_common_fruits(fruits, citrus_fruits)` that takes two lists of strings as input. The function should return the items common to both lists, sorted alphabetically, along with the total count of items in each list and the percentage of common items compared to the total number of items in both lists combined. The input lists are not guaranteed to be sorted or contain unique items.
"""

def find_common_fruits(fruits, citrus_fruits):
    common_fruits = sorted(list(set(fruits) & set(citrus_fruits)))
    total_fruits = len(fruits)
    total_citrus_fruits = len(citrus_fruits)
    common_count = len(common_fruits)
    common_percentage = (common_count / (total_fruits + total_citrus_fruits)) * 100
    return common_fruits, total_fruits, total_citrus_fruits, common_count, common_percentage
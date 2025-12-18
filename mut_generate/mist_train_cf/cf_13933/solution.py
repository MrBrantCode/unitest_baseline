"""
QUESTION:
Implement a function `count_unique_items(arr: List[int]) -> int` that takes an array of integers as input and returns the count of unique items in the array. A unique item is an item that appears only once in the array. The array may contain negative numbers, may be empty, may contain duplicate values, and may be very large. The function should have a time complexity of O(n), where n is the size of the array, and should not use any built-in Python libraries or functions that directly solve this problem.
"""

from typing import List

def count_unique_items(arr: List[int]) -> int:
    # Create a hash table to store the count of each item
    count_table = {}
    
    # Iterate through the array and update the count table
    for item in arr:
        if item in count_table:
            count_table[item] += 1
        else:
            count_table[item] = 1
    
    # Count the number of unique items
    unique_count = 0
    for count in count_table.values():
        if count == 1:
            unique_count += 1
    
    return unique_count
"""
QUESTION:
Implement a recursive function named `count_fruits_recursive` that takes a list of fruits as input, where the list can contain both integers and nested lists. The function should recursively traverse the list and its nested lists, summing up all the integers (representing the number of fruits) and returning the total count. The function should handle lists of arbitrary depth.
"""

def count_fruits_recursive(fruits, index=0, total=0):
    if index == len(fruits):
        return total
    
    if isinstance(fruits[index], int):
        total += fruits[index]
    elif isinstance(fruits[index], list):
        total += count_fruits_recursive(fruits[index])  # Recursively count fruits in nested list
    
    return count_fruits_recursive(fruits, index + 1, total)
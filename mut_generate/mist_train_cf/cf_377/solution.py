"""
QUESTION:
Write a recursive function `count_fruits_recursive` that takes a nested list of fruits where each element is either an integer (representing the number of fruits) or a list of fruits. The function should return the total number of fruits. The function can take an optional `index` parameter (default 0) and an optional `total` parameter (default 0) to track the current position and total count during recursion.
"""

def count_fruits_recursive(fruits, index=0, total=0):
    if index == len(fruits):
        return total
    
    # Check the type of fruit at the current index
    if isinstance(fruits[index], int):
        total += fruits[index]
    elif isinstance(fruits[index], list):
        total += count_fruits_recursive(fruits[index])  # Recursively count fruits in nested list
    
    return count_fruits_recursive(fruits, index + 1, total)
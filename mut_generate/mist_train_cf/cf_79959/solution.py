"""
QUESTION:
Write a function called `binary_search` that takes in a list of numbers (`data`) and a target number (`search_num`). The function should first sort the list if it is unsorted, then perform a binary search to determine if the target number exists in the list. The function should return `True` if the target number is found and `False` otherwise.
"""

def binary_search(data, search_num):
    # Sort the data first
    data.sort()
    
    # Initialize low and high pointers
    low = 0
    high = len(data) - 1
    
    while low <= high:
        # Calculate the midpoint
        mid = (low + high) // 2
        
        # If the search number is found, return True
        if data[mid] == search_num:
            return True
        # If the search number is less than the midpoint, move the high pointer to the left
        elif search_num < data[mid]:
            high = mid - 1
        # If the search number is greater than the midpoint, move the low pointer to the right
        else:
            low = mid + 1
    # If the loop completes without finding the number, it's not in the list
    return False
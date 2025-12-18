"""
QUESTION:
Write a function called `search_element` that takes two parameters: `list_a` (a sorted list of up to 1000 strings, each with a maximum length of 50 characters) and `element` (the specific string to search for). The function should return the 0-indexed position of the element in the list if found, and -1 if not found. The solution should have a time complexity of O(log n), where n is the number of elements in the list, and should not use any built-in search functions or libraries.
"""

def search_element(list_a, element):
    left = 0
    right = len(list_a) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if list_a[mid] == element:
            return mid
        
        if list_a[mid] < element:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1
"""
QUESTION:
Create a function `remove_duplicates` that takes a list as input and returns a new list containing unique elements from the original list, maintaining their order. The function should have a time complexity of O(n) and space complexity of O(n), where n is the number of elements in the list.
"""

def remove_duplicates(lst):
    unique_list = []
    seen = set()
    
    for element in lst:
        if element not in seen:
            unique_list.append(element)
            seen.add(element)
    
    return unique_list
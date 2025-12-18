"""
QUESTION:
Create a function called `remove_duplicates` that takes a list as input and returns a new list containing the unique elements from the input list in the original order. The function should have a time complexity of O(n) and a space complexity of O(n), where n is the number of elements in the list.
"""

def remove_duplicates(lst):
    unique_list = []
    seen = set()
    
    for element in lst:
        if element not in seen:
            unique_list.append(element)
            seen.add(element)
    
    return unique_list
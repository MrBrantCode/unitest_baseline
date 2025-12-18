"""
QUESTION:
Create a function called `concatenate_lists` that takes two lists as input and returns a new list containing all unique elements from both input lists without using the `extend()` or `+` methods. The function should have a time complexity of O(n), where n is the total number of elements in both lists.
"""

def concatenate_lists(list1, list2):
    combined_list = list1 + list2  
    result = []
    for element in combined_list:
        if element not in result:
            result.append(element)
    return result
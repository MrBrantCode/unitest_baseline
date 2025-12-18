"""
QUESTION:
Write a function `concatenate_lists(list1, list2)` that takes two lists as input and returns a new list containing all unique elements from both lists. The function should concatenate the lists using a for loop and without using any built-in methods such as `extend()` or `+` for concatenation, and remove any duplicate elements from the resulting list. The time complexity of the function should be O(n), where n is the total number of elements in both lists.
"""

def concatenate_lists(list1, list2):
    combined_list = []
    for element in list1:
        combined_list.append(element)
    for element in list2:
        combined_list.append(element)
    result = []
    for element in combined_list:
        if element not in result:
            result.append(element)
    return result
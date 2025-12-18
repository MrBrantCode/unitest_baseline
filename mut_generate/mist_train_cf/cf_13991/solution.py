"""
QUESTION:
Write a function named `compare_lists` that compares two lists containing integers and/or strings. The function should determine whether the two lists are equal, considering the order of elements. It should have a time complexity of O(n), where n is the length of the longer list, and a space complexity of O(1).
"""

def compare_lists(list1, list2):
    # Check if the lengths of the lists are different
    if len(list1) != len(list2):
        return False
    
    # Iterate through the elements of both lists
    for i in range(len(list1)):
        # Check if the elements at the current index are different
        if list1[i] != list2[i]:
            return False
    
    # If no differences were found, the lists are equal
    return True
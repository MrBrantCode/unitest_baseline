"""
QUESTION:
Write a function `count_common_elements(list1, list2)` that accepts two lists of non-negative integers and returns a dictionary with common integers as keys and their total counts in both lists as values. If the input lists contain non-integer or negative values, the function should return an error message. If there are no common elements, the function should return a corresponding message.
"""

def count_common_elements(list1, list2):
    # Checking if all elements in both lists are non-negative integers
    if all(isinstance(i, int) and i >= 0 for i in list1) and all(isinstance(i, int) and i >= 0 for i in list2):

        # Getting the common elements between both lists
        common_elements = list(set(list1) & set(list2))

        # Creating a dictionary to store the unique elements and their counts
        count_dict = {}
        
        # For each common element count its occurances in both lists
        for elem in common_elements:
            count1 = list1.count(elem)
            count2 = list2.count(elem)
            count_dict[elem] = count1 + count2

        # Checking if the common_elements list is empty
        if common_elements:
            return count_dict
        else:
            return "There are no common elements between the two arrays."
    else:
        return "Error: Invalid input. Please input arrays of non-negative integers only."
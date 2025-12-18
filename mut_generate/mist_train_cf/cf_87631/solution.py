"""
QUESTION:
Write a function `compare_lists(list1, list2)` that compares two lists of numbers and returns a new list with the elements common to both lists, preserving the order and count of each common element, and a list of counts for each common element. The function should have a time complexity of O(n) and a space complexity of O(n), where n is the total number of elements in both lists.
"""

def compare_lists(list1, list2):
    # Create dictionaries to store the counts of elements in each list
    count_dict1 = {}
    count_dict2 = {}
    
    # Iterate through list1 and count the occurrences of each element
    for num in list1:
        count_dict1[num] = count_dict1.get(num, 0) + 1
    
    # Iterate through list2 and count the occurrences of each element
    for num in list2:
        count_dict2[num] = count_dict2.get(num, 0) + 1
    
    # Create a new list to store the common elements
    result = []
    
    # Iterate through the keys in count_dict1
    for num in count_dict1.keys():
        # Check if the current element is in both lists
        if num in count_dict2:
            # Add the element to the new list the minimum number of times it appears in either list
            result += [num] * min(count_dict1[num], count_dict2[num])
    
    return result, [min(count_dict1[num], count_dict2[num]) for num in result]
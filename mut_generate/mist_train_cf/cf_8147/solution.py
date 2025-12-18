"""
QUESTION:
Create a function 'combineTwoLists' that takes two lists as parameters. The function should combine the two lists into a new list with unique elements, sorted in ascending order, and limited to a maximum length of 10 elements. The function should have a time complexity of O(nlogn) and a space complexity of O(n), where n is the total number of elements in the input lists.
"""

def combineTwoLists(list1, list2):
    """
    This function combines two lists into a new list with unique elements, 
    sorted in ascending order, and limited to a maximum length of 10 elements.

    Args:
        list1 (list): The first list to combine.
        list2 (list): The second list to combine.

    Returns:
        list: A combined list of unique elements, sorted in ascending order, and limited to a maximum length of 10 elements.
    """
    combinedList = list1 + list2
    combinedList = list(set(combinedList))
    combinedList = sorted(combinedList)
    
    if len(combinedList) > 10:
        combinedList = combinedList[:10]
    
    return combinedList
"""
QUESTION:
Implement a function named `sort_list` that sorts a list of positive integers in ascending order without using any built-in sorting functions or libraries. The function should have a time complexity of O(n^2).
"""

def sort_list(myList):
    """
    Sorts a list of positive integers in ascending order using the Bubble Sort algorithm.
    
    Time complexity: O(n^2)
    
    Args:
    myList (list): A list of positive integers.
    
    Returns:
    list: The sorted list in ascending order.
    """
    for i in range(len(myList) - 1):
        for j in range(len(myList) - 1 - i):
            if myList[j] > myList[j + 1]:
                myList[j], myList[j + 1] = myList[j + 1], myList[j]
    return myList
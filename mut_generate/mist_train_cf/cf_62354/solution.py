"""
QUESTION:
Implement a function called `bubble_sort` that sorts a list of elements in ascending order using the bubble sort algorithm. The function should also optimize the bubble sort algorithm to stop early if the list is already sorted. Additionally, create a helper function called `is_sorted` that validates if the list is sorted in ascending order. The `is_sorted` function should return `True` if the list is sorted and `False` otherwise. The `bubble_sort` function should return the sorted list. The input to both functions is a list of elements.
"""

def is_sorted(input_list):
    """
    This function tests whether a list is sorted in ascending order. 
    It iterates over the list and checks each pair of elements.
    If it find any pair out of order, it immediately returns False. 
    If it finishes iterating over the input_list without finding any elements out of order, it returns True.
    """
    for i in range(len(input_list) - 1): 
        if input_list[i] > input_list[i + 1]: 
            return False
    return True

def bubble_sort(input_list):
    """
    This is an implementation of the optimized bubble sort algorithm. 
    It has a while loop that continues until the list is sorted. 
    Inside this while loop, it has a for loop that iterates over each pair of adjacent elements in the list
    If it finds a pair that are out of order, it swaps them.
    Then it checks if the list is sorted. If it is, it breaks out of the while loop early. 
    This is the optimization comes into play If the list is already sorted then it doesn't need to continue the sorting process.
    """
    while not is_sorted(input_list): 
        for i in range(len(input_list) - 1): 
            if input_list[i] > input_list[i + 1]:
                input_list[i], input_list[i + 1] = input_list[i + 1], input_list[i] 
    return input_list
"""
QUESTION:
Write a function named next_smallest() that takes a list of integers as input and returns the second smallest element in the list. If the list is empty or has less than two distinct elements, the function should return None. The function should have a time complexity of O(n), where n is the number of elements in the list, and should not modify the input list.
"""

def next_smallest(lst):
    if not lst or len(lst) < 2:   
        return None 

    smallest = second_smallest = float('inf')
    for element in lst:
        if element < smallest:
            second_smallest = smallest
            smallest = element
        elif smallest < element < second_smallest:
            second_smallest = element
    
    return None if second_smallest == float('inf') else second_smallest
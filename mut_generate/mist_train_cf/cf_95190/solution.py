"""
QUESTION:
Create a function `find_second_highest_number` that takes a list of integers as input. The function should return the second highest number if it is unique, otherwise it should return the third highest number. If the list has less than two elements, the function should return None.
"""

def find_second_highest_number(lst):
    if len(lst) < 2:
        return None
    
    # Sort the list in descending order
    sorted_lst = sorted(lst, reverse=True)
    
    # Find the second highest number
    second_highest = sorted_lst[1]
    
    # Check if the second highest number is unique
    if sorted_lst.count(second_highest) > 1:
        # Find the third highest number
        third_highest = sorted_lst[sorted_lst.index(second_highest) + sorted_lst.count(second_highest)]
        return third_highest
    
    return second_highest
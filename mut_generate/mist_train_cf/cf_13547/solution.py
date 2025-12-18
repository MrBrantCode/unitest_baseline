"""
QUESTION:
Create a function named `combine_lists` that takes two lists of integers as input. The function should return a new list containing only the integers from both lists that are divisible by 3 and greater than 10. If no such integers exist, return an empty list.
"""

def combine_lists(list1, list2):
    combined_list = []
    
    for num in list1 + list2:
        if num % 3 == 0 and num > 10:
            combined_list.append(num)
    
    return combined_list
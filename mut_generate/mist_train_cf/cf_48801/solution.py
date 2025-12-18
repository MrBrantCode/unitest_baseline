"""
QUESTION:
Write a function named `list_sum` that takes a list of integers or nested lists of integers as its input parameter and returns the total sum of all the integers. The function should be able to handle the presence of nested lists and correctly accumulate their values. The input list can contain any number of nested lists.
"""

def list_sum(num_list):
    total = 0
    for i in num_list:
        if type(i) == list:  
            total += list_sum(i)  
        else:
            total += i  
    return total
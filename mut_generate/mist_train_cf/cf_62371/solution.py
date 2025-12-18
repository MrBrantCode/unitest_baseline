"""
QUESTION:
Write a function called `filter_and_count` that takes a list of integers as input and returns a dictionary where the keys are the unique positive numbers from the input list and the values are their corresponding frequencies. The function should ignore all non-positive numbers in the input list.
"""

def filter_and_count(input_list):
    result_dict = {}
    
    for num in input_list:
        if num > 0:
            if num in result_dict:
                result_dict[num] += 1
            else:
                result_dict[num] = 1
    
    return result_dict
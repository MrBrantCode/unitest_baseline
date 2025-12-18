"""
QUESTION:
Create a function `calculate_sum_and_sort` that takes two lists of equal length as input. The function should create a new list by summing corresponding elements from both input lists, remove duplicate elements, sort the unique elements in descending order, and return the result as a string with elements separated by commas. The function should also handle cases where input lists contain non-numeric elements and return an error message in such cases.
"""

def calculate_sum_and_sort(list1, list2):
    if len(list1) != len(list2):
        return "Error: lists must have equal length"
    
    new_list = []
    for i in range(len(list1)):
        if not isinstance(list1[i], (int, float)) or not isinstance(list2[i], (int, float)):
            return "Error: lists must contain numbers"
        
        new_list.append(list1[i] + list2[i])
    
    unique_sorted_list = sorted(set(new_list), reverse=True)
    
    return ', '.join(map(str, unique_sorted_list))
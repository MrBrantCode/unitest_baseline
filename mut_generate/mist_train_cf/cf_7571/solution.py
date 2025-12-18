"""
QUESTION:
Write a function called `combine_and_sort_lists` that takes two lists of equal lengths as input and returns a new list with the elements of both lists combined, without duplicates, and sorted in descending order. The function must implement a custom sorting algorithm and cannot use any built-in sorting functions or methods.
"""

def combine_and_sort_lists(list1, list2):
    combined_list = list1 + list2
    unique_list = []
    
    for element in combined_list:
        if element not in unique_list:
            unique_list.append(element)
    
    for i in range(len(unique_list)):
        for j in range(i + 1, len(unique_list)):
            if unique_list[i] < unique_list[j]:
                unique_list[i], unique_list[j] = unique_list[j], unique_list[i]
    
    return unique_list
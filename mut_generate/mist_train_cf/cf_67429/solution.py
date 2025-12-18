"""
QUESTION:
Create a function named `elaborate_merged_list` that takes two input lists as parameters and returns a new list containing all unique elements from both input lists, sorted in descending order. The function must not use Python's built-in list operations for sorting and removing duplicates.
"""

def elaborate_merged_list(input_list1: list, input_list2: list):
    merged_list = []
    for element in input_list1:
        if element not in merged_list:
            merged_list.append(element)
    for element in input_list2:
        if element not in merged_list:
            merged_list.append(element)
    
    # Perform Bubble Sort on merged_list in descending order
    for iteration in range(len(merged_list)):
        for index in range(len(merged_list)-1):
            if merged_list[index] < merged_list[index + 1]:
                merged_list[index], merged_list[index + 1] = merged_list[index + 1], merged_list[index]
    return merged_list
"""
QUESTION:
Write a function named `sort_and_find_median` that takes a tuple of integers as input. The function should sort the tuple in descending order and calculate the median of the input. The length of the tuple can be either even or odd. If the length is even, the median is the average of the two middle numbers; if it's odd, the median is the single middle number. The function should not use any built-in sort or median functions, or external libraries, and should return the sorted tuple and the median.
"""

def sort_and_find_median(input_tuple):
    # Convert tuple to list for mutability 
    input_list = list(input_tuple)
    
    # Bubble sort in descending order
    for i in range(len(input_list)):
        for j in range(len(input_list) - 1):
            if input_list[j] < input_list[j + 1]:
                input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j]
    
    # Find median
    n_len = len(input_list)
    
    if n_len % 2 == 0:
        median = (input_list[n_len // 2] + input_list[n_len // 2 - 1]) / 2
    else:
        median = input_list[n_len // 2]
    
    return tuple(input_list), median
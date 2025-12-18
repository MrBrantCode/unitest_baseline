"""
QUESTION:
Create a function named `custom_filter` that takes a 2D array of integers and a custom criteria function as input, filters the 2D array according to the custom criteria, and returns a 2D array containing the filtered elements. Each sub-array in the output should be sorted in descending order. The function should implement its own filtering and sorting algorithms without using any built-in filtering or sorting functions.
"""

def custom_filter(lst, criteria):
    result = []
    
    for sub_list in lst:
        filtered_list = []  # Contains elements of sub_list that match criteria
        for num in sub_list:
            if criteria(num):  # If num pass the criteria
                # Insert num in sorted order
                i = 0
                while i < len(filtered_list) and filtered_list[i] > num:
                    i += 1
                filtered_list.insert(i, num)
        result.append(filtered_list)
        
    return result
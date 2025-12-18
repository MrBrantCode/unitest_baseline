"""
QUESTION:
Implement a function called `merge_sort` that sorts a given list of integers in ascending order using the merge sort algorithm. The function should be able to handle lists of varying sizes and should return the sorted list. Additionally, the function should be measured for its time complexity. 

The input to the function will be a list of integers and the output should be the sorted list of integers. The time complexity of the function should be measured in seconds. There are no specific constraints on the size of the input list.
"""

def merge_sort(data_set):
    if len(data_set) <= 1:
        return data_set

    mid = len(data_set) // 2
    left_half = data_set[:mid]
    right_half = data_set[mid:]

    return merge_sorted_lists(merge_sort(left_half), merge_sort(right_half))
    
def merge_sorted_lists(left, right):
    sorted_list = []
    while left and right:
        if left[0] < right[0]:
            sorted_list.append(left[0])
            left = left[1:]
        else:
            sorted_list.append(right[0])
            right = right[1:]
    while left:
        sorted_list.append(left[0])
        left = left[1:]
    while right:
        sorted_list.append(right[0])
        right = right[1:]
    return sorted_list
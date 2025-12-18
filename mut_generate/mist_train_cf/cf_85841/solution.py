"""
QUESTION:
Write a function called `find_median` that takes a list of integers as an argument and returns the median of the elements in the list. The input list may have unsorted elements and duplicates. The solution should ideally have time complexity of O(n log n) due to sorting. Do not use any built-in functions or libraries for sorting or calculating the median. Handle edge cases where the input list may be empty or contain only one element.
"""

def find_median(input_list):
    # Check if list is empty
    if not input_list:
        return None

    # Sort the list
    input_list = merge_sort(input_list)
    
    n = len(input_list)

    # If the length of the list is even
    if n % 2 == 0:
        median1 = input_list[n//2]
        median2 = input_list[n//2 - 1]
        median = (median1 + median2)/2
    # If the length of the list is odd
    else:
        median = input_list[n//2]
    return median

def merge_sort(input_list):
    if len(input_list)<=1:
        return input_list
    mid = len(input_list)//2
    left_list = input_list[:mid]
    right_list = input_list[mid:]
    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
    return list(merge(left_list, right_list))

def merge(left, right):
    res = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else: 
            res.append(right[j])
            j += 1
    res += left[i:]
    res += right[j:]
    return res
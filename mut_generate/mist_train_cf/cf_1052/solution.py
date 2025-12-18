"""
QUESTION:
Implement a function named `modified_bubble_sort` that takes a list of integers as input, sorts the non-negative elements at even indices in descending order, removes duplicates, and returns the resulting list.
"""

def modified_bubble_sort(arr):
    # Step 1: Filter out negative numbers and even indices
    filtered_arr = [num for i, num in enumerate(arr) if i % 2 == 0 and num >= 0]
    
    # Step 2: Sort the filtered elements in descending order
    n = len(filtered_arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if filtered_arr[j] < filtered_arr[j + 1]:
                filtered_arr[j], filtered_arr[j + 1] = filtered_arr[j + 1], filtered_arr[j]
    
    # Step 3: Remove duplicates
    unique_sorted_arr = []
    for num in filtered_arr:
        if num not in unique_sorted_arr:
            unique_sorted_arr.append(num)
    
    return unique_sorted_arr
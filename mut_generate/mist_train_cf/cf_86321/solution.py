"""
QUESTION:
Implement the function `sort_and_remove_duplicates(arr)` to sort the input list of integers in descending order, remove any duplicate elements, and return the final result. The function should have a time complexity of O(n log n) and use O(n) extra space, where n is the length of the input list.
"""

def sort_and_remove_duplicates(arr):
    sorted_arr = sorted(arr, reverse=True)
    final_arr = []
    for i in range(len(sorted_arr)-1):
        if sorted_arr[i] != sorted_arr[i+1]:
            final_arr.append(sorted_arr[i])
    if sorted_arr:
        final_arr.append(sorted_arr[-1])  # Append the last element
    return final_arr
"""
QUESTION:
Create a function called `segregate_and_sort` that takes two parameters: an array and an integer `n` representing the number of partitions. The function should divide the array into `n` homogeneous sections without using built-in array division functions, sort each section, and return the sorted sections. The array should be divided as evenly as possible; if `n` does not divide the length of the array evenly, the remaining elements should be distributed among the sections. The function should not modify the original array.
"""

def segregate_and_sort(arr, n):
    sorted_arr = sorted(arr)
    partition_size = len(arr) // n
    remaining = len(arr) % n
    start_index = 0
    result = []
   
    for i in range(n):
        end_index = start_index + partition_size
        if remaining > 0:
            end_index += 1
            remaining -= 1
        result.append(sorted_arr[start_index:end_index])
        start_index = end_index
    return result
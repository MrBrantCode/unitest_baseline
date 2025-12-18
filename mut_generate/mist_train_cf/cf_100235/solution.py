"""
QUESTION:
Implement a stable sorting function called `counting_sort` that can handle duplicates in the input array without affecting the time or space complexity, and has a space complexity of O(1) when the range of input values is bounded. The function should take an array of integers as input and return the sorted array.
"""

def counting_sort(arr):
    if not arr:
        return arr

    # Find the range of values in the array
    min_val, max_val = min(arr), max(arr)
    count_arr = [0] * (max_val - min_val + 1)

    # Count the frequency of each value in the input array
    for val in arr:
        count_arr[val-min_val] += 1

    # Modify the count array to store the actual position of each value in the output array
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i-1]

    # Traverse the input array in reverse order to maintain the stability of duplicates
    output_arr = [0] * len(arr)
    for i in range(len(arr)-1, -1, -1):
        val = arr[i]
        idx = count_arr[val-min_val] - 1
        output_arr[idx] = val
        count_arr[val-min_val] -= 1

    return output_arr
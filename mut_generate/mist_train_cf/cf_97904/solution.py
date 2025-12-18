"""
QUESTION:
Implement a stable counting sort algorithm that can handle duplicates without affecting time or space complexity. The function should be named 'counting_sort' and take an array of integers as input. The space complexity should be O(k), where k is the range of values in the input array. The algorithm should maintain the relative order of equal elements in the sorted output.
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
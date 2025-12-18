"""
QUESTION:
Create a function called `max_subarray` that takes an array of integers as input and returns a tuple containing the maximum sum subarray and its starting and ending indices. The function should be able to handle arrays that include negative numbers and should have a time complexity of O(n), where n is the length of the input array.
"""

def max_subarray(arr):
    max_so_far = arr[0]
    max_ending_here = arr[0]
    start_index = end_index = 0
    temp_index = 0

    for i in range(1, len(arr)):
        if max_ending_here + arr[i] > arr[i]:
            max_ending_here += arr[i]
        else:
            max_ending_here = arr[i]
            temp_index = i

        if max_ending_here > max_so_far:
            max_so_far = max_ending_here
            start_index = temp_index
            end_index = i

    return arr[start_index:end_index+1], start_index, end_index
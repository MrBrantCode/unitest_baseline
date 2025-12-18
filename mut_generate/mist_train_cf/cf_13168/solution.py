"""
QUESTION:
Write a function `longest_subarray` that takes an array of integers as input and returns the longest subarray with an equal number of 0's and 1's, where the subarray must also contain an equal number of even and odd numbers. The function should return the subarray itself, not its length.
"""

def longest_subarray(arr):
    """
    Returns the longest subarray with an equal number of 0's and 1's, 
    and also contains an equal number of even and odd numbers.

    Args:
    arr (list): A list of integers.

    Returns:
    list: The longest subarray that meets the conditions.
    """
    max_len = 0
    count = 0
    sum_count = {0: -1}
    max_sum = 0
    
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            count += 1
        else:
            count -= 1

        if count in sum_count:
            curr_len = i - sum_count[count]
            if curr_len > max_len:
                max_len = curr_len
                max_sum = count
        else:
            sum_count[count] = i
    
    subarray = []
    for i in range(sum_count[max_sum] + 1, sum_count[max_sum] + max_len + 1):
        subarray.append(arr[i])
    
    return subarray
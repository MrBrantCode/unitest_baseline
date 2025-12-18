"""
QUESTION:
Create a function called `longest_common_contiguous_subarray` that takes two sorted integer arrays as input and returns the length of the longest common contiguous subarray. The function should have a time complexity of O(n) and space complexity of O(1). It should be able to handle cases where the arrays have duplicate values. If there are multiple longest common contiguous subarrays, the function should return the length of any one of them.
"""

def longest_common_contiguous_subarray(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    max_len = 0
    curr_len = 0

    i = 0
    j = 0

    while i < n1 and j < n2:
        if arr1[i] == arr2[j]:
            curr_len += 1
            i += 1
            j += 1
        else:
            max_len = max(max_len, curr_len)
            curr_len = 0

            if i < n1 - 1 and arr1[i + 1] == arr2[j]:
                i += 1
            elif j < n2 - 1 and arr1[i] == arr2[j + 1]:
                j += 1
            else:
                i += 1
                j += 1

    max_len = max(max_len, curr_len)
    return max_len
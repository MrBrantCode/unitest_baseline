"""
QUESTION:
Write a function `find_max_subarray_sum` that finds the maximum subarray sum within a given array, considering that the array may contain negative numbers, with a time complexity of O(n log n), where n is the size of the input array.
"""

def find_max_subarray_sum(arr):
    def find_max_crossing_subarray(arr, low, mid, high):
        left_sum = float('-inf')
        sum = 0
        for i in range(mid, low-1, -1):
            sum = sum + arr[i]
            if (sum > left_sum):
                left_sum = sum

        right_sum = float('-inf')
        sum = 0
        for i in range(mid + 1, high + 1):
            sum = sum + arr[i]
            if (sum > right_sum):
                right_sum = sum

        return max(left_sum + right_sum, left_sum, right_sum)

    def find_max_subarray_sum_helper(arr, low, high):
        if (low == high):
            return arr[low]

        mid = (low + high) // 2

        return max(find_max_subarray_sum_helper(arr, low, mid),
                   find_max_subarray_sum_helper(arr, mid+1, high),
                   find_max_crossing_subarray(arr, low, mid, high))

    return find_max_subarray_sum_helper(arr, 0, len(arr)-1)
"""
QUESTION:
Write a function `max_product_subarray(arr)` that determines the greatest product that can be obtained from a contiguous subsequence within an array of integers. The array can have up to 10^5 elements, and the integers in the array will range from -10^3 to 10^3. The function should correctly handle very large numbers and negative numbers.
"""

def max_product_subarray(arr):
    n = len(arr)
    min_ending_here = max_ending_here = max_so_far = arr[0]

    for i in range(1, n):
        if arr[i] < 0:
            max_ending_here, min_ending_here = min_ending_here, max_ending_here

        max_ending_here = max(arr[i], max_ending_here * arr[i])
        min_ending_here = min(arr[i], min_ending_here * arr[i])

        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far
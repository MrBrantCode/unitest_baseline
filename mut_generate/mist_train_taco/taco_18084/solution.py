"""
QUESTION:
Given an integer array, find three numbers whose product is maximum and output the maximum product.

Example 1:

Input: [1,2,3]
Output: 6



Example 2:

Input: [1,2,3,4]
Output: 24



Note:

The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.
"""

def find_maximum_product(nums):
    import heapq
    # Get the three largest numbers
    largest_three = heapq.nlargest(3, nums)
    # Get the two smallest numbers
    smallest_two = heapq.nsmallest(2, nums)
    # Calculate the maximum product
    max_product = max(largest_three[0] * largest_three[1] * largest_three[2], 
                      largest_three[0] * smallest_two[0] * smallest_two[1])
    return max_product
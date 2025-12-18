"""
QUESTION:
Write a function called `maxSubArraySum` that takes an array of numbers as input and returns the maximum cumulative total of a continuous subsequence within the array. The function should have a time complexity of O(n).
"""

def maxSubArraySum(a):
    max_so_far = a[0]
    curr_max = a[0]

    for i in range(1, len(a)):
        curr_max = max(a[i], curr_max + a[i])
        max_so_far = max(max_so_far,curr_max) 
        
    return max_so_far
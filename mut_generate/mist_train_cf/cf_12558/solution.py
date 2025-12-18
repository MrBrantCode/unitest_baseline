"""
QUESTION:
Create a function called `reverse_array` that takes an array of integers as input and returns a new array with the elements in reverse order. The function should have a time complexity of O(n), where n is the length of the input array.
"""

def reverse_array(nums):
    # create an empty array to store the reversed elements
    reversed_nums = []
    
    # iterate over the input array in reverse order
    for i in range(len(nums)-1, -1, -1):
        # append each element to the reversed array
        reversed_nums.append(nums[i])
    
    # return the reversed array
    return reversed_nums
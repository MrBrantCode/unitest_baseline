"""
QUESTION:
Write a function called `rearrange` that takes a list of integers as input and rearranges its elements such that no two identical numbers are adjacent to each other.
"""

def rearrange(nums):
    nums.sort() 
    length = len(nums) 
    temp = [0]*(length) 
       
    # to store indexes of nums[] 
    j, k = 0, length-1;
       
    # filling temp[] from both sides 
    for i in range(length): 
          
        if i%2==0: 
            temp[i] = nums[j] 
            j += 1
        else: 
            temp[i] = nums[k] 
            k -= 1
       
    # modify original array 
    for i in range(length): 
        nums[i] = temp[i]
    return nums
"""
QUESTION:
Write a function `find_modes` that finds the mode(s) in an array of integers. The mode is the number that appears most frequently in the array. If there are multiple numbers that appear the same maximum number of times, the function should return a list of all the modes in ascending order.

The function should have a time complexity of O(n) and should not use any built-in Python functions or libraries for finding the mode. It should also not use any additional data structures to store intermediate results, except for a dictionary to store the frequency of each number. The input array can contain both positive and negative integers, can be empty, and can contain duplicates.
"""

def find_modes(nums):
    if len(nums) == 0:  
        return []
    
    frequency = {}  
    
    max_count = 0  
    
    for num in nums:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
        
        max_count = max(max_count, frequency[num])
    
    modes = []  
    
    for num, count in frequency.items():
        if count == max_count:
            modes.append(num)
    
    return sorted(modes)
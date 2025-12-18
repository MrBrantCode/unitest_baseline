"""
QUESTION:
Write a function `find_sum_indices(array, n)` that takes an array of integers and an integer `n` as input. The function should return the indices of two numbers in the array whose sum equals `n`. If no such pair exists, the function should return `None`. The function should have a time complexity of O(n) and should not use any sorting algorithms or additional data structures beyond what is necessary.
"""

def find_sum_indices(array, n):
    complement_dict = {}
    
    for i, num in enumerate(array):
        complement = n - num
        
        if complement in complement_dict:
            return [complement_dict[complement], i]
        
        complement_dict[num] = i
    
    return None
"""
QUESTION:
Create a function named `create_histogram` that takes a list of numbers as input and returns a dictionary where each key is a unique pair of numbers from the list and the corresponding value is the count of that pair in the list. The function should have a time complexity of O(n^2) and space complexity of O(n^2), where n is the length of the input list.
"""

def create_histogram(nums):
    histogram = {}
    
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            pair = (nums[i], nums[j])
            
            if pair in histogram:
                histogram[pair] += 1
            else:
                histogram[pair] = 1
    
    return histogram
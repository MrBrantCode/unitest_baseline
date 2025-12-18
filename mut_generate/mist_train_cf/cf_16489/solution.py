"""
QUESTION:
Write a function called `create_histogram` that takes a list of numbers as input and returns a dictionary where each key is a unique pair of numbers from the list and the corresponding value is the number of times the pair appears in the list. The function should have a time complexity of O(n^2) and a space complexity of O(n^2), where n is the length of the input list. The pairs should be ordered and without duplicates, i.e., (a, b) is the same pair as (b, a) but (a, b) should be used.
"""

def create_histogram(nums):
    """
    Creates a histogram of unique pairs from a list of numbers.
    
    Args:
        nums (list): A list of numbers.
    
    Returns:
        dict: A dictionary where each key is a unique pair of numbers and the corresponding value is the number of times the pair appears.
    """
    
    histogram = {}
    
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            pair = tuple(sorted((nums[i], nums[j])))
            
            if pair in histogram:
                histogram[pair] += 1
            else:
                histogram[pair] = 1
    
    return histogram
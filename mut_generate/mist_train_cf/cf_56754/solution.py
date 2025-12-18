"""
QUESTION:
Write a function named `count_unique_most_frequent` that takes an integer array and its size as input. The function should return the quantity of distinct integers in the array and the most frequently occurring element. If there are multiple elements with the highest frequency, return the one that appears first in the array. The function should achieve a time complexity better than O(n²).
"""

def count_unique_most_frequent(nums):
    """
    Returns the quantity of distinct integers in the array and the most frequently occurring element.
    
    Args:
        nums (list): A list of integers.
    
    Returns:
        tuple: A tuple containing the count of unique elements and the most frequent element.
    """
    
    # Create a hashmap to store the count of each integer
    count = {}
    
    # Iterating over the array and counting the occurrence of each integer
    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    
    # Initializing maximum count and the most frequent element
    max_count = 0
    most_frequent = -1
    
    # Iterating over the array again
    for num in nums:
        # If this element's count is more than max
        if max_count < count[num]:
            # This element is the new most frequent element
            most_frequent = num
            max_count = count[num]
    
    # Returns the count of unique elements and most frequent element
    return len(count), most_frequent
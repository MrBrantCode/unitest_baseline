"""
QUESTION:
Design a function called `findMissingNumbers` that takes a list of integers as input and returns a list of missing integers in the range from the smallest to the largest number in the input list (inclusive), with a time complexity of O(n).
"""

def findMissingNumbers(nums):
    """
    This function takes a list of integers as input and returns a list of missing integers 
    in the range from the smallest to the largest number in the input list (inclusive).
    
    Args:
        nums (list): A list of integers.
    
    Returns:
        list: A list of missing integers in the range.
    """
    # Create a set to store the input numbers
    numbersSet = set(nums)
    
    # Find the minimum and maximum numbers in the input list
    min_num = min(nums)
    max_num = max(nums)
    
    # Create a list to store the missing numbers
    missingNumbers = []
    
    # Iterate through the range of numbers
    for num in range(min_num, max_num + 1):
        # If a number is not in the set, add it to the missing numbers list
        if num not in numbersSet:
            missingNumbers.append(num)
    
    return missingNumbers
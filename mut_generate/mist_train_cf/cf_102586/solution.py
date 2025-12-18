"""
QUESTION:
Write a function `findSecondLargest` to find the second largest element in an array. The array will contain at least two elements and may contain duplicates, with elements that can be positive, negative, or zero. The function should return the second largest element.
"""

def findSecondLargest(nums):
    """
    This function finds the second largest element in an array.
    
    Parameters:
    nums (list): A list of numbers.
    
    Returns:
    int: The second largest element in the array.
    """
    # Initialize two variables, largest and secondLargest, with the smallest possible values (-∞)
    largest = secondLargest = float('-inf')
    
    # Iterate through each element in the array
    for num in nums:
        # If the current element is larger than the largest variable, update the secondLargest variable to be the value of the largest variable, and update the largest variable to be the current element
        if num > largest:
            secondLargest = largest
            largest = num
        # If the current element is smaller than the largest variable but larger than the secondLargest variable, update the secondLargest variable to be the current element
        elif num < largest and num > secondLargest:
            secondLargest = num
    
    # Return the value of the secondLargest variable as the second largest element in the array
    return secondLargest
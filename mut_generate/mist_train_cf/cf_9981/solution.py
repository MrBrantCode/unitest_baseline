"""
QUESTION:
Write a function called `find_average` that takes an array of numbers as input and calculates the average of the numbers in the array. The function must also calculate the square of each number. What is the Big-O complexity of this function?
"""

def find_average(nums):
    """
    Calculate the average of the numbers in the input array and 
    return the average along with the squares of the numbers.

    Args:
    nums (list): A list of numbers.

    Returns:
    tuple: A tuple containing the average of the numbers and a list of squares.
    """
    total = 0
    squares = []
    
    # Iterate through the array to calculate the sum and squares
    for num in nums:
        total += num
        squares.append(num ** 2)
    
    # Calculate the average
    average = total / len(nums)
    
    return average, squares
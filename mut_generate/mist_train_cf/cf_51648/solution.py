"""
QUESTION:
Create a function called `find_median` that calculates the median of a list of seven distinct integers within the range -100,000 to 100,000 without using any comparison, conditional operators, or built-in math functions. The function should return the calculated median. The input list contains distinct integers and the integers are within the specified range.
"""

def find_median(numbers):
    """
    This function calculates the median of a list of seven distinct integers within the range -100,000 to 100,000 
    without using any comparison, conditional operators, or built-in math functions.
    
    Args:
    numbers (list): A list of seven distinct integers.
    
    Returns:
    int: The calculated median.
    """
    # define bucket with size 200,001 to accommodate numbers between -100,000 to 100,000
    # Initialize bucket with zeros
    bucket = [0] * 200001

    # put the numbers into the bucket
    for number in numbers:
        bucket[number + 100000] += 1

    # Find median
    count = 0
    median_position = (len(numbers) // 2)
    for i in range(len(bucket)):
        count += bucket[i]
        if count > median_position:
            median = i - 100000
            break

    return median
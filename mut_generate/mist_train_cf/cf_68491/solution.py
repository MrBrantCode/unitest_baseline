"""
QUESTION:
Write a function `calculate_median` that takes a list of elements as input and returns the median of the numeric elements in the list, disregarding non-numeric values. If the list contains no numeric elements, the function should return an error message. The input list can contain integers, floats, and strings.
"""

def calculate_median(nums):
    """
    Calculate the median of numeric elements in a list, disregarding non-numeric values.

    Args:
    nums (list): A list containing integers, floats, and/or strings.

    Returns:
    The median of the numeric elements in the list. If the list contains no numeric elements, returns an error message.
    """
    # Filter out non-numeric strings by checking whether each element is an instance of a number
    numeric_nums = [num for num in nums if isinstance(num, (int, float))]

    # Sort the numbers
    numeric_nums.sort()

    # Calculate the median based on the length of the number list
    try:
        if len(numeric_nums) % 2 == 0:  # If the list has an even number of elements
            median = (numeric_nums[len(numeric_nums) // 2 - 1] + numeric_nums[len(numeric_nums) // 2]) / 2
        else:  # The list has an odd number of elements
            median = numeric_nums[len(numeric_nums) // 2]

        return median
    except IndexError:  # in case all elements are non-numeric
        return "The array does not contain any numeric elements."
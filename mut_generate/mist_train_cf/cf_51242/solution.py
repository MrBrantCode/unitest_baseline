"""
QUESTION:
Write a function `find_median` that calculates the median value of five unique real numbers without using built-in or third-party library functions for statistical measures. The function should take five real numbers as input and return their median value. The numbers are not guaranteed to be in any particular order.
"""

def find_median(num1, num2, num3, num4, num5):
    """
    This function calculates the median value of five unique real numbers.
    
    Parameters:
    num1 (float): The first real number.
    num2 (float): The second real number.
    num3 (float): The third real number.
    num4 (float): The fourth real number.
    num5 (float): The fifth real number.
    
    Returns:
    float: The median value of the five real numbers.
    """
    numbers = [num1, num2, num3, num4, num5]
    for i in range(len(numbers)):
        for j in range(len(numbers) - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers[len(numbers) // 2]
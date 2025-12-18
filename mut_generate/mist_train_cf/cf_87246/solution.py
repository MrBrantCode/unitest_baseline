"""
QUESTION:
Implement a function `calculate_standard_deviation` that calculates the standard deviation of a list of integers without using built-in mathematical functions or libraries. The function should:

* Calculate the mean of the list by summing all the numbers and dividing the total by the length of the list.
* Calculate the variance by subtracting the mean from each number in the list, squaring the result, summing all the squared differences, and dividing by the length of the list.
* Calculate the standard deviation by taking the square root of the variance (using only the `** 0.5` operator).

Restrictions:
* The input list must contain at least 3 numbers.
* The input list must only contain integers. If not, raise an exception with the message "Input list should only contain integers."
* If the length of the list is less than or equal to 2, raise an exception with the message "Input list should contain at least 3 numbers."
"""

def entrance(numbers):
    if len(numbers) <= 2:
        raise Exception("Input list should contain at least 3 numbers.")
    
    for num in numbers:
        if not isinstance(num, int):
            raise Exception("Input list should only contain integers.")
    
    mean = sum(numbers) / len(numbers)
    
    variance = sum([(num - mean)**2 for num in numbers]) / len(numbers)
    
    standard_deviation = variance ** 0.5
    
    return standard_deviation
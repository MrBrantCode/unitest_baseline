"""
QUESTION:
Write a function called "calculate_result" that takes three parameters, x, y, and z, and performs the following operations in order: 
1. Adds x and y together.
2. Subtracts z from the result.
3. Multiplies the result by x.
4. Divides the result by z.
5. Adds the result to y.
6. Subtracts z from the result.
7. Raises the result to the power of x.
8. Calculates the square root of the result.
9. Rounds the result to the nearest integer.
Return the final result.
"""

def calculate_result(x, y, z):
    """
    Performs a series of operations on the input parameters and returns the final result.

    :param x: The first number.
    :param y: The second number.
    :param z: The third number.
    :return: The final result after performing all operations.
    """
    step1 = x + y
    step2 = step1 - z
    step3 = step2 * x
    step4 = step3 / z
    step5 = step4 + y
    step6 = step5 - z
    step7 = step6 ** x
    step8 = step7 ** 0.5
    step9 = round(step8)
    return step9
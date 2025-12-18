"""
QUESTION:
Create a Python function `perfect_cubes_and_digit_sums` that takes a positive integer `n` as input and returns the list of perfect cubes between 1 and `n`, the sum of digits of each perfect cube, and the average sum of the digits of all perfect cubes found. The function should not take any other inputs besides `n` and should not require any external libraries or predefined functions.
"""

def perfect_cubes_and_digit_sums(n):
    """
    This function takes a positive integer n as input and returns the list of perfect cubes between 1 and n, 
    the sum of digits of each perfect cube, and the average sum of the digits of all perfect cubes found.
    
    Args:
    n (int): A positive integer.

    Returns:
    tuple: A tuple containing a list of perfect cubes, a list of sum of digits of perfect cubes, and the average sum of digits.
    """

    def sum_of_digits(num):
        """Helper function to find the sum of digits of a number"""
        sum = 0
        while(num > 0):
            sum += num % 10
            num //= 10
        return sum

    def is_perfect_cube(num):
        """Helper function to check if a number is a perfect cube"""
        cube_root = round(num**(1/3))
        return cube_root**3 == num

    perfect_cubes = []
    sum_of_digits_list = []

    for i in range(1, n+1):
        if is_perfect_cube(i):
            perfect_cubes.append(i)
            sum_of_digits_list.append(sum_of_digits(i))

    sum_of_digits_avg = sum(sum_of_digits_list) / len(sum_of_digits_list) if sum_of_digits_list else 0

    return perfect_cubes, sum_of_digits_list, sum_of_digits_avg
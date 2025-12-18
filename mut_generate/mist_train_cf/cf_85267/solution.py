"""
QUESTION:
Create a function called `power_of_two` that calculates the first 'n' powers of two using recursion and memoization. The function should return the list of powers, the sum of the powers, and the average of the powers rounded to two decimal places. The input to the function should be the number of powers 'n'.
"""

def power_of_two(n):
    """
    This function calculates the first 'n' powers of two using recursion and memoization.
    It returns the list of powers, the sum of the powers, and the average of the powers rounded to two decimal places.

    Args:
        n (int): The number of powers to calculate.

    Returns:
        list, int, float: A list of the first 'n' powers of two, their sum, and their average.
    """

    # Define a helper function to calculate the power of two using recursion and memoization
    def calculate_power(i, memo={}):
        if i == 0:
            return 1
        if i in memo:
            return memo[i]
        memo[i] = 2 * calculate_power(i - 1, memo)
        return memo[i]

    # Generate the first 'n' powers of two and store them in a list
    powers_of_two_list = [calculate_power(i) for i in range(n)]

    # Calculate the sum of the powers of two in the list
    powers_of_two_sum = sum(powers_of_two_list)

    # Calculate the average of the powers of two rounded to two decimal places
    powers_of_two_avg = round(powers_of_two_sum / len(powers_of_two_list), 2)

    # Return the list of powers, the sum, and the average
    return powers_of_two_list, powers_of_two_sum, powers_of_two_avg
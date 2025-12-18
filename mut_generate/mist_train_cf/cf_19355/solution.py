"""
QUESTION:
Write a function `is_prime_and_sum_of_prime_digits(n)` that takes a positive integer `n` as input and returns a tuple of boolean and integer. The boolean value should indicate whether the number is prime or not, and the integer should be the sum of all prime digits in the number. The input number should be greater than or equal to 100 and less than or equal to 10^9. The prime digits are 2, 3, 5, and 7.
"""

def is_prime_and_sum_of_prime_digits(n):
    """
    This function takes a positive integer n as input and returns a tuple of boolean and integer.
    The boolean value indicates whether the number is prime or not, and the integer is the sum of all prime digits in the number.
    
    Parameters:
    n (int): A positive integer greater than or equal to 100 and less than or equal to 10^9.
    
    Returns:
    tuple: A tuple containing a boolean value indicating whether the number is prime and an integer representing the sum of prime digits.
    """

    # Function to check if a number is prime
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    # Function to calculate the sum of prime digits
    def sum_of_prime_digits(num):
        prime_digits = [2, 3, 5, 7]
        sum_of_digits = 0
        while num > 0:
            digit = num % 10
            if digit in prime_digits:
                sum_of_digits += digit
            num = num // 10
        return sum_of_digits

    # Check if the input number is prime
    is_prime_result = is_prime(n)
    
    # Calculate the sum of prime digits
    sum_of_prime_digits_result = sum_of_prime_digits(n)

    return is_prime_result, sum_of_prime_digits_result
"""
QUESTION:
Create a function called `break_down_and_check_prime` that takes a single integer as input. The function should break down the input number into its individual digits and store them as a list of integers. Additionally, the function should check whether the input number is prime. The function should return a tuple containing the list of digits and a boolean value indicating whether the number is prime.
"""

def break_down_and_check_prime(number):
    # Break down the number into its digits
    digits = [int(digit) for digit in str(number)]
    
    # Check if the number is prime
    is_prime = True
    if number < 2:
        is_prime = False
    else:
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                is_prime = False
                break
    
    # Return the digits and prime check result
    return digits, is_prime
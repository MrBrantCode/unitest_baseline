"""
QUESTION:
Design a function `check_prime(num_list)` that takes a list of integers as input and checks if any of the numbers are prime. The function should return a list of prime numbers found in the input list or a message indicating that no prime numbers were found. The function should only consider numbers greater than 1 as potential prime numbers.
"""

def check_prime(num_list):
    """
    This function checks if any numbers in the input list are prime.
    
    Args:
    num_list (list): A list of integers.
    
    Returns:
    list: A list of prime numbers found in the input list or a message indicating that no prime numbers were found.
    """
    prime_list = []
    for number in num_list:
        if number > 1:  
           for val in range(2, number):
               if (number % val) == 0:
                   break
           else:
               prime_list.append(number)
    if prime_list:
        return prime_list
    else:
        return "There are no prime numbers in the list."
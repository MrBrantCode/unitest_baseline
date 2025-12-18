"""
QUESTION:
Function Name: Calculate the product of prime numbers in a list divisible by 4.

Given a list of integers, write a function to calculate the product of all prime numbers in the list that are divisible by 4. The function should not use any built-in functions for finding the product. The list may have a maximum length of 200 elements. The algorithm must have a time complexity of O(n) and a space complexity of O(1).

The list may contain duplicate elements. A prime number is a number greater than 1 that has no positive divisors other than 1 and itself. A number is divisible by 4 if the remainder when divided by 4 is 0.
"""

def product_of_primes_divisible_by_4(mylist):
    """
    Calculate the product of prime numbers in the list that are divisible by 4.

    Args:
        mylist (list): A list of integers.

    Returns:
        int: The product of prime numbers in the list divisible by 4.
    """
    product = 1
    for num in mylist:
        if num % 4 == 0 and all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            product *= num
    return product
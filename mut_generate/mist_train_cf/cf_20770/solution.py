"""
QUESTION:
Create a function named `number_properties` that takes an integer `n` as input and determines its properties. The function should print whether the number is even or odd, whether it's prime or not, and if not prime, print its factors. Additionally, it should check if the number is a perfect square. The input number `n` should be between 1 and 1000.
"""

def number_properties(n):
    """
    This function determines the properties of a given number n.
    
    Args:
    n (int): The input number.
    
    Returns:
    None
    """

    # Check if the number is within the valid range
    if not 1 <= n <= 1000:
        print("Invalid number. Please enter a number between 1 and 1000.")
        return

    # Check if the number is even or odd
    if n % 2 == 0:
        print("This is an even number")
    else:
        print("This is an odd number")

    # Check if the number is prime or not
    factors = [i for i in range(1, n + 1) if n % i == 0]
    if len(factors) > 2:
        print("This is not a prime number")
        print("Factors:", factors)
    else:
        print("This is a prime number")

    # Check if the number is a perfect square
    if int(n ** 0.5) ** 2 == n:
        print("This is a perfect square")
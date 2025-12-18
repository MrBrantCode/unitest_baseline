"""
QUESTION:
Create a function `prime_and_mersenne(n)` that takes an integer `n` as input and determines whether the number is prime or not. If the number is not prime, the function should return the factors of the number. If the number is prime, the function should check if it is a Mersenne Prime and return the result. The function should not use any external libraries and should be able to handle numbers up to a certain limit efficiently.
"""

def prime_and_mersenne(n):
    """
    This function determines whether the number is prime or not. 
    If the number is not prime, the function returns the factors of the number. 
    If the number is prime, the function checks if it is a Mersenne Prime and returns the result.

    Args:
    n (int): The number to be checked.

    Returns:
    str: A message stating whether the number is prime or not and its factors or if it's a Mersenne Prime.
    """
    
    # Check if the number is prime
    if n <= 1:
        return f"{n} is not a prime number."
    elif n <= 3:
        # If prime, check if it's a Mersenne Prime
        i = 2
        while i <= n:
            if (2**i) - 1 == n:
                return f"{n} is a prime number and also a Mersenne Prime."
            i += 1
        return f"{n} is a prime number but not a Mersenne Prime."
    elif n % 2 == 0 or n % 3 == 0:
        # If not prime, find factors
        factors = []
        for i in range(1, n + 1):
            if n % i == 0:
                factors.append(i)
        return f"{n} is not a prime number. The factors of {n} are: {factors}."
    else:
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                # If not prime, find factors
                factors = []
                for j in range(1, n + 1):
                    if n % j == 0:
                        factors.append(j)
                return f"{n} is not a prime number. The factors of {n} are: {factors}."
            i += 6
        # If prime, check if it's a Mersenne Prime
        j = 2
        while j <= n:
            if (2**j) - 1 == n:
                return f"{n} is a prime number and also a Mersenne Prime."
            j += 1
        return f"{n} is a prime number but not a Mersenne Prime."
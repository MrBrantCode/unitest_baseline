"""
QUESTION:
Design a function `euler_totient(n)` that calculates Euler's totient function (φ) for a given integer `n`, which counts the positive integers up to `n` that are relatively prime to `n`. The function should handle all integers up to a certain dimension or limit. Implement this function in Python, ensuring it handles cases where `n` is a prime number and cases where `n` is a composite number with multiple prime factors.
"""

def euler_totient(n):
    """
    This function calculates Euler's totient function (φ) for a given integer n, 
    which counts the positive integers up to n that are relatively prime to n.

    Args:
        n (int): The input number.

    Returns:
        int: The Euler's totient of the input number.
    """

    result = n   
    p = 2
    while(p * p <= n):
        if (n % p) == 0: 
            while (n % p == 0):
                n //= p
            result *= (1.0 - (1.0 / float(p)))
        p += 1
             
    if (n > 1):
        result *= (1.0 - (1.0 / float(n)))
  
    return int(result)
"""
QUESTION:
A common problem in number theory is to find x given a such that:

a * x = 1 mod [n] 

Then x is called the inverse of a modulo n. 

Your goal is to code a function inverseMod wich take a and n as parameters and return x.

You may be interested by these pages:

http://en.wikipedia.org/wiki/Modular_multiplicative_inverse

http://en.wikipedia.org/wiki/Extended_Euclidean_algorithm


a and n should be co-prime to have a solution, if it is not the case, you should return None (Python), nil (Ruby) or null (Javascript). 

a and n will be positive integers. The problem can easily be generalised to negative integer with some sign changes so we won't deal with them.
"""

def modular_inverse(a: int, n: int) -> int:
    """
    Compute the modular inverse of 'a' under modulo 'n'.

    Parameters:
    a (int): The integer for which the modular inverse is to be computed.
    n (int): The modulus.

    Returns:
    int: The modular inverse of 'a' modulo 'n'.
    None: If 'a' and 'n' are not co-prime.
    """
    
    def egcd(a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            (g, y, x) = egcd(b % a, a)
            return (g, x - b // a * y, y)
    
    (g, x, y) = egcd(a, n)
    if g != 1:
        return None
    else:
        return x % n
"""
QUESTION:
Function: `exchange(lst1, lst2)`

The function takes in two non-empty lists of integers `lst1` and `lst2` and returns "YES" if swapping an arbitrary number of elements between the two lists makes the first list (`lst1`) have only prime numbers while keeping the total sum across both lists intact. The swap must maintain the original sequence/order of the items in their individual lists. Otherwise, it returns "NO".
"""

def exchange(lst1, lst2):
    """
    Check if swapping an arbitrary number of elements between the two lists would make 
    the first list have only prime numbers while keeping the total sum across both lists intact. 
    A swap must maintain the original sequence of the items in their individual lists.
    """
    def is_prime(n):
        """Check if a number is prime."""
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes1, nonprimes1 = [n for n in lst1 if is_prime(n)], [n for n in lst1 if not is_prime(n)]
    primes2, nonprimes2 = [n for n in lst2 if is_prime(n)], [n for n in lst2 if not is_prime(n)]
    
    for nonprime in nonprimes1:
        replaceable = [(i, prime) for i, prime in enumerate(primes2) if prime > nonprime]
        if replaceable:
            i, prime = min(replaceable, key = lambda x: x[1])
            nonprimes2.append(nonprime)
            primes2.pop(i)
        else:
            return "NO"
    
    if sum(nonprimes1 + primes1 + nonprimes2 + primes2) != sum(lst1 + lst2):
        return "NO"
    
    return "YES"
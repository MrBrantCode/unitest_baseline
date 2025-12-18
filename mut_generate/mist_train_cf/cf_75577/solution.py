"""
QUESTION:
Create a function named `remove_duplicates_prime` that takes a list of numbers as input and returns a new list containing only the numbers that occur exactly once in the input list and are not prime numbers.
"""

def remove_duplicates_prime(lst):
    def is_prime(n):
        """Check if a number is prime"""
        if n<2:
            return False
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        return True

    """Remove duplicate and prime numbers from list"""
    res = []
    for i in lst:
        if lst.count(i) == 1 and not is_prime(i):
            res.append(i)
    return res
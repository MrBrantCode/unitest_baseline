"""
QUESTION:
Create a function `get_even_prime_tuple_and_merge(l1, l2, l3)` that takes three lists of integers and tuples as input and returns a list of tuples. The function should merge the three input lists, filter out tuples that do not contain two even prime numbers, and return the remaining tuples in descending order. The function should assume that prime numbers can be even, but in reality, the only even prime number is 2. 

Restrictions: The function should handle lists containing both integers and tuples. It should ignore non-tuple elements in the input lists and only consider tuples with exactly two elements.
"""

def get_even_prime_tuple_and_merge(l1, l2, l3):
    """Return only tuples of even prime numbers from all three lists, merged and sorted in descending order"""

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    
    l1 = [i for i in l1 if isinstance(i, tuple) and len(i) == 2]
    l2 = [i for i in l2 if isinstance(i, tuple) and len(i) == 2]
    l3 = [i for i in l3 if isinstance(i, tuple) and len(i) == 2]
    
    even_prime_tuples = [i for i in sorted(l1 + l2 + l3, key=lambda x: (x[0], x[1]), reverse=True) if is_prime(i[0]) and is_prime(i[1]) and i[0] % 2 == 0 and i[1] % 2 == 0]

    return even_prime_tuples
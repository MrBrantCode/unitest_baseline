"""
QUESTION:
Write a function `prime_geomean` that takes a list `l` containing mixed elements, including positive and negative numbers and sub-lists, and returns the geometric mean of only the prime numbers present in the arrays within `l` without using any arithmetic or inbuilt math operations. The function should handle nested lists of arbitrary depth. If there are no prime numbers in the list, the function should return `None`.
"""

def prime_geomean(l: list):
    def flatten(sublist):
        """return a 1D version of a deeply nested list"""
        flat_list = []
        for item in sublist:
            if isinstance(item, list):
                flat_list.extend(flatten(item))
            else:
                flat_list.append(item)
        return flat_list

    def get_primes(sublist):
        """return a list of the prime numbers in list l"""
        primes = []
        for num in sublist:
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        break
                else:
                    primes.append(num)
        return primes

    def multiply(sublist):
        """return the product of all the elements in list l"""
        product = 1
        for num in sublist:
            product *= num
        return product

    def nth_root(n, a):
        """calculated nth root of a"""
        return a ** (1 / n)

    primes = get_primes(flatten(l))
    if not primes:
        return None
    return nth_root(len(primes), multiply(primes))
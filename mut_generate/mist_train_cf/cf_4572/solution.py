"""
QUESTION:
Calculate the factorial of n using a recursive function with the following conditions:

- The function should check if n is a positive integer and raise an exception if it is not.
- The function should use a caching mechanism to store previously calculated factorial values.
- The caching mechanism should be implemented using a customized data structure with the following properties:
  - Constant time lookup and insertion
  - Evicts the least recently used factorial value when its capacity is reached.
- The capacity of the cache should be set to a fixed number determined by the user input.
- The function should handle the scenario when the cache is full and a new factorial value needs to be inserted.
- The time complexity of the function should be O(log n) or better.
"""

from collections import OrderedDict

def factorial(n, capacity):
    if not isinstance(n, int) or n <= 0:
        raise Exception("n should be a positive integer.")
    
    cache = OrderedDict()
    
    def fact(n):
        if n == 0 or n == 1:
            return 1
        if n in cache:
            result = cache.pop(n)
            cache[n] = result
            return result
        result = n * fact(n - 1)
        if len(cache) >= capacity:
            cache.popitem(last=False)
        cache[n] = result
        return result

    return fact(n)
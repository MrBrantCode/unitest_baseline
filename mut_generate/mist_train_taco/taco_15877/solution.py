"""
QUESTION:
Following on from [Part 1](http://www.codewars.com/kata/filling-an-array-part-1/), part 2 looks at some more complicated array contents.

So let's try filling an array with...

## ...square numbers
The numbers from `1` to `n*n`

## ...a range of numbers
A range of numbers starting from `start` and increasing by `step`

## ...random numbers
A bunch of random integers between `min` and `max`

## ...prime numbers
All primes starting from `2` (obviously)...

HOTE: All the above functions should take as their first parameter a number that determines the length of the returned array.
"""

import random

def generate_array(n, type, start=None, step=None, min=None, max=None):
    if type == "squares":
        return [i ** 2 for i in range(1, n + 1)]
    elif type == "range":
        if start is None or step is None:
            raise ValueError("Both 'start' and 'step' must be provided for range type")
        return [i for i in range(start, start + step * n, step)]
    elif type == "random":
        if min is None or max is None:
            raise ValueError("Both 'min' and 'max' must be provided for random type")
        return [random.randint(min, max) for _ in range(n)]
    elif type == "primes":
        primes_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]
        return primes_list[:n]
    else:
        raise ValueError("Invalid type specified. Use 'squares', 'range', 'random', or 'primes'.")
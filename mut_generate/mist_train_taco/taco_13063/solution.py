"""
QUESTION:
Given an array of positive or negative integers 

 I= [i1,..,in]

you have to produce a sorted array P of the form 

[ [p, sum of all ij of I for which p is a prime factor (p positive) of ij] ...]

P will be sorted by increasing order of the prime numbers.
The final result has to be given as a string in Java, C#, C, C++ and as an array of arrays in other languages.

Example:

```python
I = [12, 15] # result = [[2, 12], [3, 27], [5, 15]]
```

[2, 3, 5] is the list of all prime factors of the elements of I, hence the result.

**Notes:**
- It can happen that a sum is 0 if some numbers are negative!

Example: I = [15, 30, -45]
5 divides 15, 30 and (-45) so 5 appears in the result, the sum of the numbers for which 5 is a factor is 0 so we have [5, 0] in the result amongst others. 

- In Fortran - as in any other language - the returned string is not permitted to contain any redundant trailing whitespace: you can use dynamically allocated character strings.
"""

def sum_for_prime_factors(lst):
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    factors = {i for k in lst for i in range(2, abs(k) + 1) if k % i == 0}
    prime_factors = {i for i in factors if is_prime(i)}
    return [[p, sum(e for e in lst if e % p == 0)] for p in sorted(prime_factors)]
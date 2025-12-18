"""
QUESTION:
Backwards Read Primes are primes that when read backwards in base 10 (from right to left) 
are a different prime. (This rules out primes which are palindromes.)
```
Examples:
13 17 31 37 71 73 are Backwards Read Primes
```
13 is such because it's prime and read from right to left writes 31 which is prime too. Same for the others.

## Task
Find all Backwards Read Primes between two positive given numbers (both inclusive), the second one always being greater than or equal to the first one. The resulting array or the resulting string will be ordered following the natural order of the prime numbers.

## Example

backwardsPrime(2, 100) => [13, 17, 31, 37, 71, 73, 79, 97] 
backwardsPrime(9900, 10000) => [9923, 9931, 9941, 9967]
backwardsPrime(501, 599) => []

## Note for Forth
Return only the first backwards-read prime between start and end
or 0 if you don't find any

```python
backwards_prime(2, 100) => [13, 17, 31, 37, 71, 73, 79, 97] 
backwards_prime(9900, 10000) => [9923, 9931, 9941, 9967]
```
"""

def find_backwards_primes(start, stop):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def reverse(n):
        return int(''.join(str(n)[::-1]))

    primes = []
    for n in range(start, stop + 1):
        if is_prime(n):
            reversed_n = reverse(n)
            if is_prime(reversed_n) and n != reversed_n:
                primes.append(n)
                if start <= reversed_n <= stop and reversed_n not in primes:
                    primes.append(reversed_n)
    
    return sorted(set(primes))
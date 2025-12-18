"""
QUESTION:
We need a function ```prime_bef_aft()``` that gives the largest prime below a certain given value ```n```, 

```befPrime or bef_prime``` (depending on the language), 

and the smallest prime larger than this value, 

```aftPrime/aft_prime``` (depending on the language).

The result should be output in a list like the following:

```python
prime_bef_aft(n) == [befPrime, aftPrime]
```

If n is a prime number it will give two primes, n will not be included in the result.

Let's see some cases:
```python
prime_bef_aft(100) == [97, 101]

prime_bef_aft(97) == [89, 101]

prime_bef_aft(101) == [97, 103]
```
Range for the random tests: 
```1000 <= n <= 200000```

(The extreme and special case n = 2 will not be considered for the tests. Thanks Blind4Basics)

Happy coding!!
"""

def is_prime(a):
    if a < 2:
        return False
    if a == 2 or a == 3:
        return True
    if a % 2 == 0 or a % 3 == 0:
        return False
    max_divisor = int(a ** 0.5)
    (d, i) = (5, 2)
    while d <= max_divisor:
        if a % d == 0:
            return False
        d += i
        i = 6 - i
    return True

def find_prime_neighbors(n):
    bef_prime = None
    aft_prime = None
    
    # Find the largest prime below n
    for num in range(n - 1, 1, -1):
        if is_prime(num):
            bef_prime = num
            break
    
    # Find the smallest prime above n
    for num in range(n + 1, 3 * n):
        if is_prime(num):
            aft_prime = num
            break
    
    return [bef_prime, aft_prime]
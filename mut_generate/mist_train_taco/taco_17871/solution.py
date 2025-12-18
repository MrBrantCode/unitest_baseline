"""
QUESTION:
In this Kata, you will be given a number and your task will be to return the nearest prime number. 

```Haskell
solve(4) = 3. The nearest primes are 3 and 5. If difference is equal, pick the lower one. 
solve(125) = 127
```

We'll be testing for numbers up to `1E10`. `500` tests.

More examples in test cases. 

Good luck!

If you like Prime Katas, you will enjoy this Kata: [Simple Prime Streaming](https://www.codewars.com/kata/5a908da30025e995880000e3)
"""

def find_nearest_prime(n):
    def is_prime(p):
        if p <= 1:
            return False
        if p == 2:
            return True
        if p % 2 == 0:
            return False
        for x in range(3, int(p ** 0.5) + 1, 2):
            if p % x == 0:
                return False
        return True
    
    if is_prime(n):
        return n
    
    step = n % 2 + 1
    while True:
        if is_prime(n - step):
            return n - step
        elif is_prime(n + step):
            return n + step
        else:
            step += 2
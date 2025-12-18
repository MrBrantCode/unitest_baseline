"""
QUESTION:
Every number may be factored in prime factors.

For example, the number 18 may be factored by its prime factors ``` 2 ``` and ```3```
```
18 = 2 . 3 . 3 = 2 . 3²
```
The sum of the prime factors of 18 is  ```2 + 3 + 3 = 8```

But some numbers like 70 are divisible by the sum of its prime factors:
```
70 = 2 . 5 . 7 # sum of prime factors = 2 + 5 + 7 = 14
and 70 is a multiple of 14
```
Of course that primes would fulfill this property, but is obvious, because the prime decomposition of a number, is the number itself and every number is divisible by iself. That is why we will discard every prime number in the results

We are interested in collect the integer positive numbers (non primes) that have this property in a certain range ```[a, b]``` (inclusive).

Make the function ```mult_primefactor_sum()```, that receives the values ```a```, ```b``` as limits of the range ```[a, b]``` and ```a < b``` and outputs the sorted list of these numbers.

Let's see some cases:
```python
mult_primefactor_sum(10, 100) == [16, 27, 30, 60, 70, 72, 84] 

mult_primefactor_sum(1, 60) == [1, 4, 16, 27, 30, 60]
```
"""

def mult_primefactor_sum(a, b):
    def factorize_add(num):
        if num < 4:
            return num
        d = 2
        p = 0
        while d < num ** 0.5 + 1:
            while not num % d:
                p += d
                num /= d
            d += 1 if d == 2 else 2
        return p if num == 1 else p + num
    
    result = []
    for i in range(a, b + 1):
        r = factorize_add(i)
        if r != i and i % r == 0:
            result.append(i)
    return result
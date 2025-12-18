"""
QUESTION:
This kata is inspired on the problem #50 of the Project Euler. 

The prime ``` 41```  is the result of the sum of many consecutive primes.

In fact, ``` 2 + 3 + 5 + 7 + 11 + 13 = 41 , (6 addens)   ``` 

Furthermore, the prime ``` 41```  is the prime below ``` 100 (val_max)```  that has the longest chain of consecutive prime addens.

The prime with longest chain of addens for ```val_max = 500``` is ```499``` with ```17``` addens. 

In fact:
```3+5+7+11+13+17+19+23+29+31+37+41+43+47+53+59+61= 499```

Find the function ```prime_maxlength_chain()```(primeMaxlengthChain() javascript), that receives an argument ```val_max```, the upper limit, all the found primes should be less than ```val_max``` and outputs this found prime.

Let's see some cases:
```python
prime_maxlength_chain(100) == [41]
prime_maxlength_chain(500) == [499]
```
If we have more than one prime with these features, the function should output an array with the found primes sorted.
```python
prime_maxlength_chain(499) == [379, 491]
```
Random Tests for `val_max` (`valMax`)
```
100 ≤ val_max ≤ 500.000
```
Enjoy it!
"""

def prime_maxlength_chain(val_max):
    LIMIT = 500000
    sieve = [True] * (LIMIT // 2)
    
    # Sieve of Eratosthenes to find all primes up to LIMIT
    for n in range(3, int(LIMIT ** 0.5) + 1, 2):
        if sieve[n // 2]:
            sieve[n * n // 2::n] = [False] * ((LIMIT - n * n - 1) // 2 // n + 1)
    
    # List of all primes up to LIMIT
    PRIMES = [2] + [2 * i + 1 for i in range(1, LIMIT // 2) if sieve[i]]
    
    if val_max < 5:
        return []
    
    found = []
    
    # Determine the maximum possible size of the chain
    for n in range(2, 400):
        if sum(PRIMES[:n]) >= val_max:
            max_size = n
            break
    
    # Check chains of decreasing size
    for size in range(max_size, 1, -1):
        if size % 2 == 0:
            n = sum(PRIMES[:size])
            if n < val_max and n in PRIMES:
                return [n]
        else:
            for start in range(1, max_size - size + 1):
                n = sum(PRIMES[start:start + size])
                if n < val_max and n in PRIMES:
                    found.append(n)
            if found:
                return sorted(found)
    
    return []
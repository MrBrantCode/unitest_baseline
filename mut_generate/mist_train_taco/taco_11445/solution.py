"""
QUESTION:
Goldbach's conjecture is one of the oldest and best-known unsolved problems in number theory and all of mathematics. It states:

Every even integer greater than 2 can be expressed as the sum of two primes.
For example: 

`6 = 3 + 3`
`8 = 3 + 5`
`10 = 3 + 7 = 5 + 5`
`12 = 5 + 7`

Some rules for the conjecture: 

- pairs should be descending like [3,5] not [5,3]

- all pairs should be in ascending order based on the first element of the pair: 
`[[5, 13], [7, 11]]` is accepted 
but `[[7, 11],[5, 13]]` is not accepted.

Write the a function that find all identical pairs of prime numbers:
```python
def goldbach(even_number)
```
You should return an array of containing pairs of primes, like:
```python
[[5, 13], [7, 11]]  # even_number = 18
```
or
```python
[[3, 31], [5, 29], [11, 23], [17, 17]] # even_number = 34
```
"""

def find_goldbach_pairs(even_number):
    if even_number < 4 or even_number % 2 != 0:
        return []
    
    if even_number == 4:
        return [[2, 2]]
    
    l = even_number - 2
    sieve = [True] * (l // 2)
    
    for i in range(3, int(l ** 0.5) + 1, 2):
        if sieve[i // 2]:
            sieve[i * i // 2::i] = [False] * ((l - i * i - 1) // (2 * i) + 1)
    
    primes = [2 * i + 1 for i in range(1, l // 2) if sieve[i]]
    
    pairs = [[p, even_number - p] for p in primes if even_number - p in primes and p <= even_number - p]
    
    return pairs
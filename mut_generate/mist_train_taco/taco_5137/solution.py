"""
QUESTION:
Write a class Random that does the following:

1. Accepts a seed
```python
>>> random = Random(10)
>>> random.seed
10
```

2. Gives a random number between 0 and 1
```python
>>> random.random()
0.347957
>>> random.random()
0.932959
```

3. Gives a random int from a range
```python
>>> random.randint(0, 100)
67
>>> random.randint(0, 100)
93
```

Modules `random` and `os` are forbidden.
Dont forget to give feedback and your opinion on this kata even if you didn't solve it!
"""

import hashlib

def generate_random_numbers(seed, num_random, num_randint, start, end):
    HASH_MAX = (1 << 32 * 4) - 1
    random_numbers = []
    randint_numbers = []
    
    for _ in range(num_random):
        x = int(hashlib.md5(str(seed).encode()).hexdigest(), 16)
        seed += 1
        random_numbers.append(x / HASH_MAX)
    
    for _ in range(num_randint):
        x = int(hashlib.md5(str(seed).encode()).hexdigest(), 16)
        seed += 1
        randint_numbers.append(start + int((x / HASH_MAX) * (end + 1 - start)))
    
    return random_numbers, randint_numbers
"""
QUESTION:
Jzzhu has picked n apples from his big apple tree. All the apples are numbered from 1 to n. Now he wants to sell them to an apple store. 

Jzzhu will pack his apples into groups and then sell them. Each group must contain two apples, and the greatest common divisor of numbers of the apples in each group must be greater than 1. Of course, each apple can be part of at most one group.

Jzzhu wonders how to get the maximum possible number of groups. Can you help him?


-----Input-----

A single integer n (1 ≤ n ≤ 10^5), the number of the apples.


-----Output-----

The first line must contain a single integer m, representing the maximum number of groups he can get. Each of the next m lines must contain two integers — the numbers of apples in the current group.

If there are several optimal answers you can print any of them.


-----Examples-----
Input
6

Output
2
6 3
2 4

Input
9

Output
3
9 3
2 4
6 8

Input
2

Output
0
"""

def max_apple_groups(n):
    if n == 1:
        return (0, [])
    
    # Generate primes up to n/2
    primes = [x for x in range(2, int(n / 2) + 1) if all((x % y != 0 for y in range(2, int(x ** 0.5) + 1)))]
    primes = primes[::-1]
    
    # Initialize used dictionary
    used = {i: False for i in range(2, n + 1)}
    
    outputs = []
    counter = 0
    
    for prime in primes:
        multiples = []
        for x in range(1, n // prime + 1):
            if not used[prime * x]:
                multiples.append(prime * x)
                used[prime * x] = True
        
        if len(multiples) % 2 == 0:
            for j in range(0, len(multiples), 2):
                outputs.append((multiples[j], multiples[j + 1]))
                counter += 1
        else:
            multiples.pop(1)
            used[prime * 2] = False
            for j in range(0, len(multiples), 2):
                outputs.append((multiples[j], multiples[j + 1]))
                counter += 1
    
    return (counter, outputs)
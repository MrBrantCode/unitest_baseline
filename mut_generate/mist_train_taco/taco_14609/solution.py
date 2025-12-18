"""
QUESTION:
Kate has a set $S$ of $n$ integers $\{1, \dots, n\} $. 

She thinks that imperfection of a subset $M \subseteq S$ is equal to the maximum of $gcd(a, b)$ over all pairs $(a, b)$ such that both $a$ and $b$ are in $M$ and $a \neq b$. 

Kate is a very neat girl and for each $k \in \{2, \dots, n\}$ she wants to find a subset that has the smallest imperfection among all subsets in $S$ of size $k$. There can be more than one subset with the smallest imperfection and the same size, but you don't need to worry about it. Kate wants to find all the subsets herself, but she needs your help to find the smallest possible imperfection for each size $k$, will name it $I_k$. 

Please, help Kate to find $I_2$, $I_3$, ..., $I_n$.


-----Input-----

The first and only line in the input consists of only one integer $n$ ($2\le n \le 5 \cdot 10^5$)  — the size of the given set $S$.


-----Output-----

Output contains only one line that includes $n - 1$ integers: $I_2$, $I_3$, ..., $I_n$.


-----Examples-----
Input
2

Output
1 
Input
3

Output
1 1 


-----Note-----

First sample: answer is 1, because $gcd(1, 2) = 1$.

Second sample: there are subsets of $S$ with sizes $2, 3$ with imperfection equal to 1. For example, $\{2,3\}$ and $\{1, 2, 3\}$.
"""

def find_smallest_imperfections(n):
    # Initialize a list to mark primes
    primes = [0] * (n + 1)
    
    # Sieve of Eratosthenes to find primes
    for i in range(2, n + 1):
        if primes[i] == 0:
            primes[i] = 1
            for j in range(i * 2, n + 1, i):
                primes[j] = -1
    
    # Extract the prime numbers
    primes = [i for (i, p) in enumerate(primes) if p == 1]
    
    # Initialize the result list
    res = [0] * (n + 1)
    
    # Set the smallest imperfection for primes to 1
    for p in primes:
        res[p] = 1
    
    # Calculate the smallest imperfection for non-prime numbers
    for p in primes:
        for j in range(p * 2, n + 1, p):
            if res[j] == 0:
                res[j] = max(p, j // p)
    
    # Return the result excluding the first two elements (0 and 1)
    return res[2:]
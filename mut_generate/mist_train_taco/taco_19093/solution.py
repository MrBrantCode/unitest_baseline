"""
QUESTION:
Taru and Chandu both are getting bored. So Taru thinks to play a game and he gives a number to Chandu and asks him to find the number of combinations formed by divisors in form of prime.     
For example:-
For N   = 36 divisor in form of prime are ( 2 , 2 , 3 , 3 )
Number of combinations formed by prime divisor of 36 are 8.
Check the sample I/O for better understanding.

INPUT-
Number of test cases T. Next T lines contain a number N.

OUTPUT-
Number of different combinations formed by divisors in form of prime of N. 

CONSTRAINTS-
1 ≤ T ≤ 100
1 ≤N ≤ 10^12

SAMPLE INPUT
1
36

SAMPLE OUTPUT
8

Explanation

2,2,3,3  are divisors in form of prime for 36 and different/unique combinations formed are -
(2) , (3) , (2,3) , (2,2) , (2,2,3) , (3,3) , (2,2,3,3) , (2,3,3).
"""

def count_prime_divisor_combinations(N):
    n = int(N ** 0.5) + 1
    prime_divisors = []
    
    # Find prime divisors
    for i in range(2, n):
        while N % i == 0:
            prime_divisors.append(i)
            N //= i
    
    if N > 1:
        prime_divisors.append(N)
    
    # Count the number of combinations
    from collections import Counter
    prime_count = Counter(prime_divisors)
    
    combinations = 1
    for count in prime_count.values():
        combinations *= (count + 1)
    
    return combinations
"""
QUESTION:
Chester Bennington, being a skinny kid as we all know, is always bullied since he was a child. This time its just unacceptable. Mike Shinoda, the second vocalist to his band, tried to bully him. Chester was never a bright student and Mike, being a high school graduate, gave him a tough mathematical problem. He gave Chester a number N. His task is to find all the prime numbers under N(inclusive) which can be written as the sum of two primes and list them.

Help Chester so that this time he is not bullied....... Again !!!

Input: First line contains t, the number of test cases. t lines follow after that which contain an integer N.

Output: For each test case, you have to print all the prime numbers that meet the above mentioned condition in a single line in a space separated format. For each test-case use a new line.

Constraints:

1 ≤ t ≤ 100

1 ≤ N ≤ 10000

Note: 1 and 0 are not considered Primes

Problem Setter: Rohit Mishra

SAMPLE INPUT
3
7
17
29

SAMPLE OUTPUT
5 7
5 7 13
5 7 13 19

Explanation

Consider test case - 2
N=17
Prime Numbers under 17 are 2,3,5,7,11,13,17
Output is 5,7,13

As 1+10 = 2+9 = 3+8 = 4+7 = 5+6 = 11
None of the above mentioned pairs meets the required criteria.
Same is the case with the other numbers which are not mentioned in the output.
"""

import math

def find_prime_sum_primes(t, test_cases):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    maxi = max(test_cases)
    primes = [j for j in range(2, maxi + 1) if is_prime(j)]
    
    prime_sum_primes = []
    for j in primes:
        for k in primes:
            if k <= j:
                continue
            if k + j > maxi:
                break
            if is_prime(k + j):
                if k + j not in prime_sum_primes:
                    prime_sum_primes.append(k + j)
    
    results = []
    for n in test_cases:
        results.append([x for x in prime_sum_primes if x <= n])
    
    return results
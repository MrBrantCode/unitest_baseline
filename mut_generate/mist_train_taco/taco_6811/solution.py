"""
QUESTION:
Alice has learnt factorization recently. Bob doesn't think she has learnt it properly and hence he has decided to quiz her. Bob gives Alice a very large number and asks her to find out the number of factors of that number. To make it a little easier for her, he represents the number as a product of N numbers. Alice is frightened of big numbers and hence is asking you for help. Your task is simple. Given N numbers, you need to tell the number of distinct factors of the product of these N numbers.

------ Input: ------ 

First line of input contains a single integer T, the number of test cases.

Each test starts with a line containing a single integer N.
The next line consists of N space separated integers (A_{i}).

------ Output: ------ 

For each test case, output on a separate line the total number of factors of the product of given numbers.

------ Constraints: ------ 

1 ≤ T ≤ 100
1 ≤ N ≤ 10
2 ≤ A_{i} ≤ 1000000

------ Scoring: ------ 

You will be awarded 40 points for correctly solving for A_{i} ≤ 100.

You will be awarded another 30 points for correctly solving for A_{i} ≤ 10000.

The remaining 30 points will be awarded for correctly solving for A_{i} ≤ 1000000.

----- Sample Input 1 ------ 
3
3
3 5 7
3
2 4 6
2
5 5
----- Sample Output 1 ------ 
8
10
3
"""

import math
from collections import Counter

def count_factors_of_product(test_cases):
    results = []
    
    for case in test_cases:
        N, A = case
        l = []
        
        for i in A:
            for j in range(2, int(i ** 0.5) + 1):
                while i % j == 0:
                    l.append(j)
                    i //= j
            if i > 1:
                l.append(i)
        
        c = Counter(l)
        r = 1
        for i in c:
            r *= c[i] + 1
        
        results.append(r)
    
    return results
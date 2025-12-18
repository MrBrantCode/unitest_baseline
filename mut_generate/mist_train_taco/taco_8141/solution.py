"""
QUESTION:
While Omar was studying for Math lectures, he found the following problem.  
Given 3 Integers N_1, N_2, N_3, count the number of common divisors which divide all of them. 

Can you please help Omar in solving this problem, because he usually sleeps in lectures. 

Input:

Given an integer T, which indicates the number of test cases.
For each test case: given 3 separated integers N_1, N_2, N_3.  

Output:

For each test case: print the number of common divisors which divide N_1, N_2, N_3. Print each case in a separate line. 

** Constraints:**  

1 ≤ T ≤ 50  
1 ≤ minimum\; (N_1, N_2 , N_3) ≤ 10 ^ {12}  
1 ≤ maximum\; (N_1, N_2 , N_3) ≤ 10 ^ {18}   

SAMPLE INPUT
1
2 4 6

SAMPLE OUTPUT
2
"""

from functools import reduce

def factors(n):
    return list(set(reduce(list.__add__, 
                    ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))

def count_common_divisors(N1, N2, N3):
    num = sorted([N1, N2, N3])
    fact = sorted(factors(num[0]), reverse=True)
    
    for d in fact:
        if all(n % d == 0 for n in num):
            return len(factors(d))
    
    return 0
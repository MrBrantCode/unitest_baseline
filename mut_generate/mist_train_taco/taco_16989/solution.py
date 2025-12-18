"""
QUESTION:
Motu and Patlu are racing against each other on a circular track of radius $R$. Initially they are at the same point on the track and will run in same direction .The coach ordered them to run $X$ rounds of the circular field. Patlu wants to know how many times they will meet after the race starts and  before any of them finishes $X$ rounds. But he is busy in warm up so he wants you to calculate this. You are given speed of both Motu and Patlu ($A$ and $B$). 

-----Input:-----
- First line will contain $T$, number of testcases. Then the testcases follow. 
- Each testcase contains of a single line of input, four integers $X, R, A, B$. 

-----Output:-----
For each testcase, output in a single line answer the number of times whey will meet before any of them completes $X$ rounds.

-----Constraints-----
- $1 \leq T \leq 1000$
- $1 \leq R \leq 10^9$
- $1 \leq X \leq 10^9$
- $1 \leq A \leq 10^9$
- $1 \leq B \leq 10^9$
- Speed of both are different

-----Sample Input:-----
2
3 10 2 5
2 20 5 10

-----Sample Output:-----
1
0
"""

import math

def calculate_meetings(T, test_cases):
    def swap(a, b):
        return (b, a)
    
    results = []
    
    for i in range(T):
        x, r, a, b = test_cases[i]
        peri = 2 * r
        tp = x * peri
        
        if a < b:
            (a, b) = swap(a, b)
        
        t1 = tp / a
        d2 = t1 * b
        dd = abs(tp - d2)
        
        if dd % peri == 0:
            results.append(int(dd // peri) - 1)
        else:
            n = int(dd // peri)
            results.append(n)
    
    return results
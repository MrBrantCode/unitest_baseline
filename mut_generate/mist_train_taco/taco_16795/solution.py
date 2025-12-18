"""
QUESTION:
You are given an array $a$ consisting of $n$ positive integers. You have to choose a positive integer $d$ and paint all elements into two colors. All elements which are divisible by $d$ will be painted red, and all other elements will be painted blue.

The coloring is called beautiful if there are no pairs of adjacent elements with the same color in the array. Your task is to find any value of $d$ which yields a beautiful coloring, or report that it is impossible.


-----Input-----

The first line contains a single integer $t$ ($1 \le t \le 1000$) — the number of testcases.

The first line of each testcase contains one integer $n$ ($2 \le n \le 100$) — the number of elements of the array.

The second line of each testcase contains $n$ integers $a_1, a_2, \dots, a_n$ ($1 \le a_i \le 10^{18}$).


-----Output-----

For each testcase print a single integer. If there is no such value of $d$ that yields a beautiful coloring, print $0$. Otherwise, print any suitable value of $d$ ($1 \le d \le 10^{18}$).


-----Examples-----

Input
5
5
1 2 3 4 5
3
10 5 15
3
100 10 200
10
9 8 2 6 6 2 8 6 5 4
2
1 3
Output
2
0
100
0
3


-----Note-----

None
"""

from math import gcd
from functools import reduce

def find_beautiful_coloring_d(test_cases):
    results = []
    
    for case in test_cases:
        n, a = case
        g = 0
        g1 = 0
        
        # Calculate gcd for even indices
        for i in range(0, n, 2):
            g = gcd(g, a[i])
        
        # Calculate gcd for odd indices
        for i in range(1, n, 2):
            g1 = gcd(g1, a[i])
        
        if g == g1:
            results.append(0)
        else:
            fl = 0
            fl1 = 0
            
            # Check if g is valid
            for i in range(1, n, 2):
                if a[i] % g == 0:
                    fl = 1
                    break
            
            # Check if g1 is valid
            for i in range(0, n, 2):
                if a[i] % g1 == 0:
                    fl1 = 1
                    break
            
            if fl and fl1:
                results.append(0)
            elif fl:
                results.append(g1)
            else:
                results.append(g)
    
    return results
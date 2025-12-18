"""
QUESTION:
The MarkiT online virtual market startup wants to organize its grand opening in NIT Patna.
but they want maximum crowd for their inauguration. So the manager told  this  to Praveen a student in NITP who suggested them:
The first-year students come to campus  every x hour,
Second-year students come to campus every y hour,
Third-year students come to campus every z hour and 
Fourth-year is very busy so they don't come regularly.
So Praveen being very clever told him the no of times in n days he can have an audience of all year student (1st,2nd & 3rd) at max. So can you code what Praveen has done?

-----Input:-----
- First line will contain $T$, number of testcases. Then the testcases follow. 
- Each testcase contains of a 2 line of input, first line contain one  integers $N$ (No of Days). 
-Next line contain 3 space separated integer the  value of x y z

-----Output:-----
For each testcase, output in a single line answer the no of times audience consists of all year.

-----Constraints-----
- $1 \leq T \leq 1000$
- $1 \leq N \leq 10^8$
- $1 \leq x,y,z \leq 10^5$

-----Sample Input:-----
1
10
8 10 6

-----Sample Output:-----
2

-----EXPLANATION:-----
First favourable condition will come on 5th day and Second on 10th day.
"""

import math

def calculate_max_audience_times(T, test_cases):
    def fun(num1, num2):
        if num1 > num2:
            a = num1
            b = num2
        else:
            a = num2
            b = num1
        rem = a % b
        while rem != 0:
            a = b
            b = rem
            rem = a % b
        gcd = b
        return int(num1 * num2 / gcd)
    
    results = []
    for case in test_cases:
        N, x, y, z = case
        hours = N * 24
        lcm = x
        lcm = fun(x, y)
        lcm = fun(lcm, z)
        results.append(int(hours // lcm))
    
    return results
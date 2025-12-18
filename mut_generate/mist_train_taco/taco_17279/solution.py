"""
QUESTION:
You are given a sequence of non-negative integers $A_1, A_2, \ldots, A_N$. At most once, you may choose a non-negative integer $X$ and for each valid $i$, change $A_i$ to $A_i \oplus X$ ($\oplus$ denotes bitwise XOR).
Find the minimum possible value of the sum of all elements of the resulting sequence.

-----Input-----
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of the input contains a single integer $N$.
- The second line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.

-----Output-----
For each test case, print a single line containing one integer ― the minimum possible sum.

-----Constraints-----
- $1 \le T \le 1,000$
- $1 \le N \le 10^5$
- $1 \le A_i \le 10^9$ for each valid $i$
- the sum of $N$ over all test cases does not exceed $10^6$

-----Subtasks-----
Subtask #1 (50 points):
- $1 \le N \le 10^3$
- $1 \le A_i \le 10^3$ for each valid $i$
Subtask #2 (50 points): original constraints

-----Example Input-----
3
5
2 3 4 5 6
4
7 7 7 7
3
1 1 3

-----Example Output-----
14
0
2

-----Explanation-----
Example case 1: If we choose $X = 6$, the sequence becomes $(4, 5, 2, 3, 0)$.
Example case 2: We can choose $X = 7$ to make all elements of the resulting sequence equal to $0$.
Example case 3: We can choose $X = 1$. The sequence becomes $(0, 0, 2)$, with sum $2$.
"""

from collections import defaultdict

def minimum_possible_sum(test_cases):
    results = []
    
    for case in test_cases:
        N, A = case
        bin_count = defaultdict(int)
        total = 0
        max_length = 0
        
        for num in A:
            bin_value = '{0:0b}'.format(num)
            temp = len(bin_value) - 1
            if max_length < len(bin_value):
                max_length = len(bin_value)
            for b in bin_value:
                if b == '1':
                    bin_count[temp] += 1
                temp -= 1
        
        for i in range(max_length):
            total += pow(2, i) * min(bin_count[i], N - bin_count[i])
        
        results.append(total)
    
    return results
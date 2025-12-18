"""
QUESTION:
We have N camels numbered 1,2,\ldots,N. Snuke has decided to make them line up in a row.

The happiness of Camel i will be L_i if it is among the K_i frontmost camels, and R_i otherwise.

Snuke wants to maximize the total happiness of the camels. Find the maximum possible total happiness of the camel.

Solve this problem for each of the T test cases given.

Constraints

* All values in input are integers.
* 1 \leq T \leq 10^5
* 1 \leq N \leq 2 \times 10^{5}
* 1 \leq K_i \leq N
* 1 \leq L_i, R_i \leq 10^9
* The sum of values of N in each input file is at most 2 \times 10^5.

Input

Input is given from Standard Input in the following format:


T
\mathrm{case}_1
\vdots
\mathrm{case}_T


Each case is given in the following format:


N
K_1 L_1 R_1
\vdots
K_N L_N R_N


Output

Print T lines. The i-th line should contain the answer to the i-th test case.

Example

Input

3
2
1 5 10
2 15 5
3
2 93 78
1 71 59
3 57 96
19
19 23 16
5 90 13
12 85 70
19 67 78
12 16 60
18 48 28
5 4 24
12 97 97
4 57 87
19 91 74
18 100 76
7 86 46
9 100 57
3 76 73
6 84 93
1 6 84
11 75 94
19 15 3
12 11 34


Output

25
221
1354
"""

import heapq
from operator import itemgetter

def calculate_max_happiness(T, test_cases):
    results = []
    
    for case in test_cases:
        N = len(case)
        res = 0
        camel_left = []
        camel_right = []
        
        for K, L, R in case:
            res += min(L, R)
            if R <= L:
                camel_left.append([K, L, R])
            elif K != N:
                camel_right.append([N - K, L, R])
        
        camel_left.sort(key=itemgetter(0))
        camel_right.sort(key=itemgetter(0))
        
        hq = []
        i = 0
        for j in range(1, N + 1):
            while i < len(camel_left) and camel_left[i][0] == j:
                heapq.heappush(hq, camel_left[i][1] - camel_left[i][2])
                i += 1
            while len(hq) > j:
                heapq.heappop(hq)
        res += sum(hq)
        
        hq = []
        i = 0
        for j in range(1, N):
            while i < len(camel_right) and camel_right[i][0] == j:
                heapq.heappush(hq, camel_right[i][2] - camel_right[i][1])
                i += 1
            while len(hq) > j:
                heapq.heappop(hq)
        res += sum(hq)
        
        results.append(res)
    
    return results
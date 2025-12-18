"""
QUESTION:
Alice has recently learned in her economics class that the market is said to be in equilibrium when the supply is equal to the demand.

Alice has market data for N time points in the form of two integer arrays S and D. Here, S_{i} denotes the supply at the i^{th} point of time and D_{i} denotes the demand at the i^{th} point of time, for each 1 ≤ i ≤ N.

Help Alice in finding out the number of time points at which the market was in equilibrium. 

------ Input Format ------ 

- The first line of input will contain an integer T — the number of test cases. The description of T test cases follows.
- Each test case contains three lines of input.
- The first line of each test case contains an integer N, the length of the arrays S and D.
- The second line of each test case contains N space-separated integers S_{1}, S_{2}, \ldots , S_{N}.
- The third line of each test case contains N space-separated integers D_{1}, D_{2}, \ldots , D_{N}. 

------ Output Format ------ 

For each test case, output the number of time points at which the market was in equilibrium.

------ Constraints ------ 

$1 ≤ T ≤ 10$
$1 ≤ N ≤ 100$
$1 ≤ S_{i}, D_{i} ≤ 100$ for every $1 ≤ i ≤ N$

----- Sample Input 1 ------ 
2
4
1 2 3 4
2 1 3 4
4
1 1 2 2
1 2 1 1
----- Sample Output 1 ------ 
2
1
----- explanation 1 ------ 
Test case $1$: For $i = 3$ and $i = 4$, we have supply equal to demand, hence the market is in equilibrium.

Test case $2$: For $i = 1$, we have supply equal to demand, hence the market is in equilibrium.
"""

def count_equilibrium_points(test_cases):
    results = []
    for case in test_cases:
        N = case['N']
        supplies = case['S']
        demands = case['D']
        equilibrium_count = 0
        for i in range(N):
            if supplies[i] == demands[i]:
                equilibrium_count += 1
        results.append(equilibrium_count)
    return results
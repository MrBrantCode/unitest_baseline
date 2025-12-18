"""
QUESTION:
You are given an integer $D$. Find an integer sequence $A_1, A_2, \ldots, A_N$ such that the following conditions are satisfied:
- $1 \le N \le 10^5$
- $1 \le A_i \le 10^5$ for each valid $i$
- $\sum_{i=1}^N \sum_{j=i}^N \left( \mathrm{min}(A_i, A_{i+1}, \ldots, A_j) - \mathrm{GCD}(A_i, A_{i+1}, \ldots, A_j) \right) = D$
It can be proved that a solution always exists under the given constraints.
Note: $\mathrm{GCD}(B_1, B_2, \ldots, B_M)$ is the greatest integer which divides all the integers $B_1, B_2, \ldots, B_M$.

-----Input-----
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains a single integer $D$.

-----Output-----
For each test case, print two lines. The first of these lines should contain a single integer $N$. The second line should contain $N$ space-separated integers $A_1, A_2, \ldots, A_N$.
If there are multiple solutions, you may find any one of them.

-----Constraints-----
- $1 \le T \le 10$
- $0 \le D \le 10^9$

-----Example Input-----
4
2
5
200
13

-----Example Output-----
3
3 3 2 
5
2 8 5 1 10 
7
12 10 15 11 19 13 15
4
5 4 4 10
"""

def generate_sequence(D: int) -> tuple[int, list[int]]:
    """
    Generates an integer sequence A_1, A_2, ..., A_N such that the sum of the minimum of subarrays minus the GCD of subarrays equals D.

    Parameters:
    D (int): The target value for the sum of the minimum of subarrays minus the GCD of subarrays.

    Returns:
    tuple[int, list[int]]: A tuple containing the length of the sequence N and the sequence A.
    """
    P = 10 ** 5 - 2
    ans = []
    
    if D == 0:
        ans.append(1)
    
    while D > 0:
        P = min(P, D)
        ans.append(P + 2)
        ans.append(P + 1)
        ans.append(1)
        D = D - P
    
    return len(ans), ans
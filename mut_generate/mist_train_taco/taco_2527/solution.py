"""
QUESTION:
Anya loves to fold and stick. Today she decided to do just that.

Anya has n cubes lying in a line and numbered from 1 to n from left to right, with natural numbers written on them. She also has k stickers with exclamation marks. We know that the number of stickers does not exceed the number of cubes.

Anya can stick an exclamation mark on the cube and get the factorial of the number written on the cube. For example, if a cube reads 5, then after the sticking it reads 5!, which equals 120.

You need to help Anya count how many ways there are to choose some of the cubes and stick on some of the chosen cubes at most k exclamation marks so that the sum of the numbers written on the chosen cubes after the sticking becomes equal to S. Anya can stick at most one exclamation mark on each cube. Can you do it?

Two ways are considered the same if they have the same set of chosen cubes and the same set of cubes with exclamation marks.


-----Input-----

The first line of the input contains three space-separated integers n, k and S (1 ≤ n ≤ 25, 0 ≤ k ≤ n, 1 ≤ S ≤ 10^16) — the number of cubes and the number of stickers that Anya has, and the sum that she needs to get. 

The second line contains n positive integers a_{i} (1 ≤ a_{i} ≤ 10^9) — the numbers, written on the cubes. The cubes in the input are described in the order from left to right, starting from the first one. 

Multiple cubes can contain the same numbers.


-----Output-----

Output the number of ways to choose some number of cubes and stick exclamation marks on some of them so that the sum of the numbers became equal to the given number S.


-----Examples-----
Input
2 2 30
4 3

Output
1

Input
2 2 7
4 3

Output
1

Input
3 1 1
1 1 1

Output
6



-----Note-----

In the first sample the only way is to choose both cubes and stick an exclamation mark on each of them.

In the second sample the only way is to choose both cubes but don't stick an exclamation mark on any of them.

In the third sample it is possible to choose any of the cubes in three ways, and also we may choose to stick or not to stick the exclamation mark on it. So, the total number of ways is six.
"""

from collections import defaultdict

def count_ways_to_sum(n, k, S, A):
    # Precompute factorials up to 18!
    fact = [1]
    for i in range(1, 20):
        fact.append(fact[i - 1] * i)
    
    # Initialize dynamic programming tables
    ldp = [[defaultdict(int) for _ in range(k + 1)] for _ in range(2)]
    ldp[0][0][0] = 1
    
    # Process the first half of the cubes
    for i in range(n // 2):
        for j in range(k + 1):
            ldp[~i & 1][j].clear()
        for j in range(k + 1):
            for key in ldp[i & 1][j]:
                ldp[~i & 1][j][key] += ldp[i & 1][j][key]
                ldp[~i & 1][j][key + A[i]] += ldp[i & 1][j][key]
                if j + 1 <= k and A[i] <= 18:
                    ldp[~i & 1][j + 1][key + fact[A[i]]] += ldp[i & 1][j][key]
    
    # Initialize dynamic programming tables for the second half
    rdp = [[defaultdict(int) for _ in range(k + 1)] for _ in range(2)]
    rdp[0][0][0] = 1
    
    # Process the second half of the cubes
    for i in range(n - n // 2):
        for j in range(k + 1):
            rdp[~i & 1][j].clear()
        for j in range(k + 1):
            for key in rdp[i & 1][j]:
                rdp[~i & 1][j][key] += rdp[i & 1][j][key]
                rdp[~i & 1][j][key + A[n // 2 + i]] += rdp[i & 1][j][key]
                if j + 1 <= k and A[n // 2 + i] <= 18:
                    rdp[~i & 1][j + 1][key + fact[A[n // 2 + i]]] += rdp[i & 1][j][key]
    
    # Calculate the final answer
    ans = 0
    for i in range(k + 1):
        for key in ldp[n // 2 & 1][i]:
            for j in range(0, k - i + 1):
                ans += ldp[n // 2 & 1][i][key] * rdp[n - n // 2 & 1][j][S - key]
    
    return ans
"""
QUESTION:
Chef has a number N, Cheffina challenges the chef to check the divisibility of all the permutation of N by 2. If any of the permutations is divisible by 2 then print 1 else print 0.

-----Input:-----
- First-line will contain $T$, the number of test cases. Then the test cases follow. 
- Each test case contains a single line of input, $N$. 

-----Output:-----
For each test case, output in a single line answer 1 or 0.

-----Constraints-----
- $1 \leq T \leq 10^6$
- $1 \leq N \leq 10^6$

-----Sample Input:-----
2
19
385

-----Sample Output:-----
0
1
"""

def is_any_permutation_divisible_by_2(N: int) -> int:
    while N > 0:
        if N % 10 % 2 == 0:
            return 1
        N = N // 10
    return 0
"""
QUESTION:
A permutation $p_1,p_2...p_N$ of $\{1, 2, ..., N\}$ is beautiful if $p_i \& p_{i+1}$ is greater than 0 for every $1 \leq i < N$ . You are given an integer $N$, and your task is toconstruct a beautiful permutation of length $N$ or determine that it's impossible.
Note that $a \& b$ denotes the bitwise AND of $a$ and $b$.

-----Input:-----
First line will contain $T$, number of testcases. Then the testcases follow. 
Each testcase contains a single line of input, an integer $N$.

-----Output:-----
For each test case output $-1$ if there is no suitable permutation of length $N$, otherwise output $N$ integers in a single line which form a beautiful permutation. If there are multiple answers output any of them.

-----Constraints-----
- $1 \leq N \leq 10^5$
- The sum of $N$ over all test cases does not exceed $10^6$

-----Subtasks-----
- 50 points : $1 \leq N,T \leq 9$
- 50 points : Original constraints

-----Sample Input:-----
3
4
3
5

-----Sample Output:-----
-1
1 3 2
2 3 1 5 4
"""

def generate_beautiful_permutations(T, N_list):
    def ispoweroftwo(y):
        return math.ceil(math.log(y, 2)) == math.floor(math.log(y, 2))
    
    results = []
    
    for n in N_list:
        a = []
        if ispoweroftwo(n) and n != 1:
            results.append([-1])
            continue
        if n == 1:
            results.append([1])
            continue
        if n >= 3 and (not ispoweroftwo(n)):
            a.append(2)
            a.append(3)
            a.append(1)
        if n > 3 and (not ispoweroftwo(n)):
            i = 4
            while i <= n:
                if ispoweroftwo(i):
                    a.append(i + 1)
                    a.append(i)
                    i += 2
                else:
                    a.append(i)
                    i += 1
        results.append(a)
    
    return results
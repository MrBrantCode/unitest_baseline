"""
QUESTION:
Chef has a sequence of positive integers $A_1, A_2, \ldots, A_N$. He wants to split this sequence into two non-empty (not necessarily contiguous) subsequences $B$ and $C$ such that $\mathrm{GCD}\,(B) + \mathrm{GCD}\,(C)$ is maximum possible. Help him find this maximum value.
Note: The greatest common divisor (GCD) of a sequence of positive integers is the largest positive integer that divides each element of this sequence. For example, the GCD of the sequence $(8, 12)$ is $4$.

-----Input-----
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- The second line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.

-----Output-----
For each test case, print a single line containing one integer — the maximum value of $\mathrm{GCD}\,(B) + \mathrm{GCD}\,(C)$.

-----Constraints-----
- $1 \le T \le 10$
- $2 \le N \le 10^5$
- $1 \le A_i \le 10^9$ for each valid $i$

-----Subtasks-----
Subtask #1 (20 points): $2 \le N \le 20$
Subtask #2 (80 points): original constraints

-----Example Input-----
1              
4                    
4 4 7 6                    

-----Example Output-----
9

-----Explanation-----
Example case 1: For example, the sequence $A$ can be divided into subsequences $B = (4, 4, 6)$ and $C = (7)$.
"""

def gcd(x, y):
    while x != 0 and y != 0:
        z = y
        y = x % y
        x = z
    return x + y

def compute_other_gcd(A, gcd1):
    ret = 0
    for x in A:
        if x % gcd1 != 0:
            ret = gcd(ret, x)
    if ret == 0:
        return A[-1]
    return ret

def max_gcd_sum(A):
    A.sort()
    d = 1
    answer = 0
    while d * d <= A[0]:
        if A[0] % d == 0:
            answer = max(answer, d + compute_other_gcd(A, d))
            answer = max(answer, A[0] // d + compute_other_gcd(A, A[0] // d))
        d += 1
    return answer
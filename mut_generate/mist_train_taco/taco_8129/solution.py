"""
QUESTION:
You are given three integers n, k, m and m conditions (l_1, r_1, x_1), (l_2, r_2, x_2), ..., (l_m, r_m, x_m).

Calculate the number of distinct arrays a, consisting of n integers such that: 

  * 0 ≤ a_i < 2^k for each 1 ≤ i ≤ n; 
  * bitwise AND of numbers a[l_i] \& a[l_i + 1] \& ... \& a[r_i] = x_i for each 1 ≤ i ≤ m. 



Two arrays a and b are considered different if there exists such a position i that a_i ≠ b_i. 

The number can be pretty large so print it modulo 998244353.

Input

The first line contains three integers n, k and m (1 ≤ n ≤ 5 ⋅ 10^5, 1 ≤ k ≤ 30, 0 ≤ m ≤ 5 ⋅ 10^5) — the length of the array a, the value such that all numbers in a should be smaller than 2^k and the number of conditions, respectively.

Each of the next m lines contains the description of a condition l_i, r_i and x_i (1 ≤ l_i ≤ r_i ≤ n, 0 ≤ x_i < 2^k) — the borders of the condition segment and the required bitwise AND value on it.

Output

Print a single integer — the number of distinct arrays a that satisfy all the above conditions modulo 998244353.

Examples

Input


4 3 2
1 3 3
3 4 6


Output


3


Input


5 2 3
1 3 2
2 5 0
3 3 3


Output


33

Note

You can recall what is a bitwise AND operation [here](https://en.wikipedia.org/wiki/Bitwise_operation#AND).

In the first example, the answer is the following arrays: [3, 3, 7, 6], [3, 7, 7, 6] and [7, 3, 7, 6].
"""

def count_distinct_arrays(n, k, m, conditions):
    mod = 998244353
    ans = 1
    
    for bit in range(k):
        one = [0] * (n + 1)
        zero_cond = [0] * (n + 1)
        
        for (l, r, x) in conditions:
            if x >> bit & 1:
                one[l - 1] += 1
                one[r] -= 1
            else:
                zero_cond[r] = max(zero_cond[r], l)
        
        for i in range(n):
            one[i + 1] += one[i]
        
        dp = [0] * (n + 1)
        dp[0] = 1
        cs = [0] * (n + 2)
        cs[1] = 1
        R = 0
        
        for i in range(n):
            if not one[i]:
                dp[i + 1] = (cs[i + 1] - cs[R]) % mod
            cs[i + 2] = (cs[i + 1] + dp[i + 1]) % mod
            R = max(R, zero_cond[i + 1])
        
        ans = ans * (cs[-1] - cs[R]) % mod % mod
    
    return ans
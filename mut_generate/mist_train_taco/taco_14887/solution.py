"""
QUESTION:
Professor Dumbledore is helping Harry destroy the Horcruxes. He went to Gaunt Shack as he suspected a Horcrux to be present there. He saw Marvolo Gaunt's Ring and identified it as a Horcrux. Although he destroyed it, he is still affected by its curse. Professor Snape is helping Dumbledore remove the curse. For this, he wants to give Dumbledore exactly x drops of the potion he made. 

Value of x is calculated as maximum of p·a_{i} + q·a_{j} + r·a_{k} for given p, q, r and array a_1, a_2, ... a_{n} such that 1 ≤ i ≤ j ≤ k ≤ n. Help Snape find the value of x. Do note that the value of x may be negative.


-----Input-----

First line of input contains 4 integers n, p, q, r ( - 10^9 ≤ p, q, r ≤ 10^9, 1 ≤ n ≤ 10^5).

Next line of input contains n space separated integers a_1, a_2, ... a_{n} ( - 10^9 ≤ a_{i} ≤ 10^9).


-----Output-----

Output a single integer the maximum value of p·a_{i} + q·a_{j} + r·a_{k} that can be obtained provided 1 ≤ i ≤ j ≤ k ≤ n.


-----Examples-----
Input
5 1 2 3
1 2 3 4 5

Output
30

Input
5 1 2 -3
-1 -2 -3 -4 -5

Output
12



-----Note-----

In the first sample case, we can take i = j = k = 5, thus making the answer as 1·5 + 2·5 + 3·5 = 30.

In second sample case, selecting i = j = 1 and k = 5 gives the answer 12.
"""

def calculate_max_potion_drops(n, p, q, r, a):
    m_inf = float('-inf')
    dp = [[m_inf, m_inf, m_inf] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        dp[i][0] = max(dp[i - 1][0], a[i - 1] * p)
        dp[i][1] = max(dp[i - 1][1], dp[i][0] + a[i - 1] * q)
        dp[i][2] = max(dp[i - 1][2], dp[i][1] + a[i - 1] * r)
    
    return dp[n][2]
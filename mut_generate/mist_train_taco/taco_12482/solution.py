"""
QUESTION:
You have a password which you often type — a string s of length n. Every character of this string is one of the first m lowercase Latin letters.

Since you spend a lot of time typing it, you want to buy a new keyboard.

A keyboard is a permutation of the first m Latin letters. For example, if m = 3, then there are six possible keyboards: abc, acb, bac, bca, cab and cba.

Since you type your password with one finger, you need to spend time moving your finger from one password character to the next. The time to move from character s_i to character s_{i+1} is equal to the distance between these characters on keyboard. The total time you have to spend typing the password with a keyboard is called the slowness of this keyboard.

More formaly, the slowness of keyboard is equal to ∑_{i=2}^{n} |pos_{s_{i-1}} - pos_{s_i} |, where pos_x is position of letter x in keyboard.

For example, if s is aacabc and the keyboard is bac, then the total time of typing this password is |pos_a - pos_a| + |pos_a - pos_c| + |pos_c - pos_a| + |pos_a - pos_b| + |pos_b - pos_c| = |2 - 2| + |2 - 3| + |3 - 2| + |2 - 1| + |1 - 3| = 0 + 1 + 1 + 1 + 2 = 5.

Before buying a new keyboard you want to know the minimum possible slowness that the keyboard can have. 

Input

The first line contains two integers n and m (1 ≤ n ≤ 10^5, 1 ≤ m ≤ 20).

The second line contains the string s consisting of n characters. Each character is one of the first m Latin letters (lowercase).

Output

Print one integer – the minimum slowness a keyboard can have.

Examples

Input


6 3
aacabc


Output


5


Input


6 4
aaaaaa


Output


0


Input


15 4
abacabadabacaba


Output


16

Note

The first test case is considered in the statement.

In the second test case the slowness of any keyboard is 0.

In the third test case one of the most suitable keyboards is bacd.
"""

def calculate_minimum_slowness(n, m, s):
    INF = 10 ** 9
    count = [[0] * m for _ in range(m)]
    ord_a = ord('a')
    
    # Count transitions between characters
    for (c1, c2) in zip(s, s[1:]):
        c1 = ord(c1) - ord_a
        c2 = ord(c2) - ord_a
        if c1 != c2:
            count[c1][c2] += 1
    
    # Precompute sum of subsets
    sum_of_subset = [[0] * (1 << m) for _ in range(m)]
    for i in range(m):
        for j in range(1 << m):
            if j == 0:
                continue
            lsb = j & -j
            sum_of_subset[i][j] = sum_of_subset[i][j ^ lsb] + count[i][lsb.bit_length() - 1]
    
    # Compute adjacency in subsets
    adj_in_subset = [0] * (1 << m)
    for i in range(1 << m):
        for j in range(m):
            if i & 1 << j:
                adj_in_subset[i] += sum_of_subset[j][i]
    
    total_adj = adj_in_subset[-1]
    dp = [INF] * (1 << m)
    dp[0] = 0
    
    # Dynamic programming to find minimum slowness
    for i in range(1 << m):
        for j in range(m):
            if i & 1 << j:
                continue
            cost = total_adj - adj_in_subset[i] - adj_in_subset[~i]
            dp[i | 1 << j] = min(dp[i | 1 << j], dp[i] + cost)
    
    return dp[-1]
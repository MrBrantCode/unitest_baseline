"""
QUESTION:
You are given three integers k, p_{a} and p_{b}.

You will construct a sequence with the following algorithm: Initially, start with the empty sequence. Each second, you do the following. With probability p_{a} / (p_{a} + p_{b}), add 'a' to the end of the sequence. Otherwise (with probability p_{b} / (p_{a} + p_{b})), add 'b' to the end of the sequence.

You stop once there are at least k subsequences that form 'ab'. Determine the expected number of times 'ab' is a subsequence in the resulting sequence. It can be shown that this can be represented by P / Q, where P and Q are coprime integers, and $Q \neq 0 \operatorname{mod}(10^{9} + 7)$. Print the value of $P \cdot Q^{-1} \operatorname{mod}(10^{9} + 7)$.


-----Input-----

The first line will contain three integers integer k, p_{a}, p_{b} (1 ≤ k ≤ 1 000, 1 ≤ p_{a}, p_{b} ≤ 1 000 000).


-----Output-----

Print a single integer, the answer to the problem.


-----Examples-----
Input
1 1 1

Output
2

Input
3 1 4

Output
370000006



-----Note-----

The first sample, we will keep appending to our sequence until we get the subsequence 'ab' at least once. For instance, we get the sequence 'ab' with probability 1/4, 'bbab' with probability 1/16, and 'aab' with probability 1/8. Note, it's impossible for us to end with a sequence like 'aabab', since we would have stopped our algorithm once we had the prefix 'aab'. 

The expected amount of times that 'ab' will occur across all valid sequences is 2. 

For the second sample, the answer is equal to $\frac{341}{100}$.
"""

def calculate_expected_ab_subsequences(k, pa, pb):
    mod = 1000000007
    N = 1005
    dp = [[0 for _ in range(N)] for _ in range(N)]

    def fast_expo(a, b):
        ret = 1
        while b:
            if b % 2 == 1:
                ret = ret * a % mod
            b //= 2
            a = a * a % mod
        return ret

    def inv(x):
        return fast_expo(x, mod - 2) % mod

    def dp_val(a, b):
        if b >= k:
            return b
        return dp[a][b]

    for i in range(k):
        dp[k][i] = (i + k + pa * inv(pb)) % mod
    den = inv(pa + pb)
    for i in range(k - 1, 0, -1):
        for j in range(k - 1, -1, -1):
            dp[i][j] = pa * dp_val(i + 1, j) * den % mod + pb * dp_val(i, i + j) * den % mod
            dp[i][j] %= mod

    return dp[1][0]
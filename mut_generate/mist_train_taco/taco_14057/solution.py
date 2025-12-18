"""
QUESTION:
Let S(n) denote the number that represents the digits of n in sorted order. For example, S(1) = 1, S(5) = 5, S(50394) = 3459, S(353535) = 333555.

Given a number X, compute <image> modulo 109 + 7.

Input

The first line of input will contain the integer X (1 ≤ X ≤ 10700).

Output

Print a single integer, the answer to the question.

Examples

Input

21


Output

195


Input

345342


Output

390548434

Note

The first few values of S are 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 11, 12, 13, 14, 15, 16, 17, 18, 19, 2, 12. The sum of these values is 195.
"""

def compute_s_modulo(X: str) -> int:
    num_list = [int(digit) for digit in X]
    myMod = 10 ** 9 + 7
    length = len(num_list)
    
    f = [0] * (length + 1)
    t = [1] * (length + 1)
    
    for i in range(length):
        f[i + 1] = (f[i] * 10 + 1) % myMod
        t[i + 1] = t[i] * 10 % myMod
    
    ans = 0
    
    for i in range(1, 10):
        dp = [0] * (length + 1)
        for j in range(length):
            dp[j + 1] = (dp[j] * i + (10 - i) * (dp[j] * 10 + t[j])) % myMod
        
        c = 0
        ctr = 0
        
        for k in num_list:
            z = min(i, k)
            o = k - z
            ans += o * (dp[length - 1 - ctr] * t[c + 1] + f[c + 1] * t[length - 1 - ctr]) % myMod
            ans += z * (dp[length - 1 - ctr] * t[c] + f[c] * t[length - 1 - ctr]) % myMod
            ans %= myMod
            c += k >= i
            ctr += 1
        
        ans += f[c]
        if ans >= myMod:
            ans -= myMod
    
    return ans
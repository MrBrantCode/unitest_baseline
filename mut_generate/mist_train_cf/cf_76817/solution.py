"""
QUESTION:
Create a function called `countNumbersWithUniqueDigits` that takes an integer `n` as input, where `0 <= n <= 10`, and returns the count of all numbers with unique even digits in the range `0 <= x <= 10^n`. The function should not include numbers with repeating even digits.
"""

def countNumbersWithUniqueDigits(n):
    dp = [[0] * 1024 for _ in range(11)]
    dp[0][0] = 1

    for i in range(10):
        mask = 1 << i
        for j in range(n + 1):
            for f in range(1024):
                if dp[j][f] == 0:
                    continue

                for k in range(10):
                    if (f & (1 << k)) != 0:
                        continue
                    if i * 2 == j and k == 0:
                        continue
                    nf = f | (1 << k)
                    dp[j + 1 if k % 2 == 0 else j][nf] += dp[j][f]
    
    return sum(dp[i][1023] for i in range(n // 2 * 2 + 1, n + 1))
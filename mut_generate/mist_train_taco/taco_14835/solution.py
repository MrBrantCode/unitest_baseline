"""
QUESTION:
Given is a string S. Each character in S is either a digit (0, ..., 9) or ?.
Among the integers obtained by replacing each occurrence of ? with a digit, how many have a remainder of 5 when divided by 13? An integer may begin with 0.
Since the answer can be enormous, print the count modulo 10^9+7.

-----Constraints-----
 - S is a string consisting of digits (0, ..., 9) and ?.
 - 1 \leq |S| \leq 10^5

-----Input-----
Input is given from Standard Input in the following format:
S

-----Output-----
Print the number of integers satisfying the condition, modulo 10^9+7.

-----Sample Input-----
??2??5

-----Sample Output-----
768

For example, 482305, 002865, and 972665 satisfy the condition.
"""

def count_integers_with_remainder_5(S: str) -> int:
    MOD = 10 ** 9 + 7
    old_dp = [0] * 13
    new_dp = [0] * 13
    old_dp[0] = 1
    
    for c in S:
        for i in range(13):
            if c == '?':
                for d in range(10):
                    new_dp[(i * 10 + d) % 13] += old_dp[i]
            else:
                new_dp[(i * 10 + int(c)) % 13] += old_dp[i]
        
        old_dp = [x % MOD for x in new_dp]
        new_dp = [0] * 13
    
    return old_dp[5]
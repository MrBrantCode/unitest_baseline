"""
QUESTION:
Given is an integer S.
Find how many sequences there are whose terms are all integers greater than or equal to 3, and whose sum is equal to S.
The answer can be very large, so output it modulo 10^9 + 7.

-----Constraints-----
 - 1 \leq S \leq 2000
 - All values in input are integers.

-----Input-----
Input is given from Standard Input in the following format:
S

-----Output-----
Print the answer.

-----Sample Input-----
7

-----Sample Output-----
3

3 sequences satisfy the condition: \{3,4\}, \{4,3\} and \{7\}.
"""

def count_sequences(S: int) -> int:
    if S < 3:
        return 0
    
    mod = 10**9 + 7
    DP = [0] * (S + 1)
    DP[3] = 1
    
    for i in range(4, S + 1):
        DP[i] = (DP[i - 1] + DP[i - 3]) % mod
    
    return DP[S]
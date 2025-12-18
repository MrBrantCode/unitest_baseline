"""
QUESTION:
We have a string S of length N consisting of A, B, and C.
You can do the following operation on S zero or more times:
 - Choose i (1 \leq i \leq |S| - 1) such that S_i \neq S_{i + 1}. Replace S_i with the character (among A, B, and C) that is different from both S_i and S_{i + 1}, and remove S_{i + 1} from S.
Find the number of distinct strings that S can be after zero or more operations, and print the count modulo (10^9+7).

-----Constraints-----
 - 1 \leq N \leq 10^6
 - S is a string of length N consisting of A, B, and C.

-----Input-----
Input is given from Standard Input in the following format:
N
S

-----Output-----
Print the number of distinct strings that S can be after zero or more operations, modulo (10^9+7).

-----Sample Input-----
5
ABAAC

-----Sample Output-----
11

For example, the following sequence of operations turns S into ACB:
 - First, choose i=2. We replace S_2 with C and remove S_3, turning S into ACAC.
 - Then, choose i=3. We replace S_3 with B and remove S_4, turning S into ACB.
"""

def count_distinct_strings(N, S):
    MOD = 10 ** 9 + 7
    
    # Convert the string S into a list of indices for 'A', 'B', 'C'
    s = list(map('_ABC'.index, S))
    
    # Initialize the first character and the dp array
    s0 = s[0]
    dp = [0, 0, 0, 0]
    dp[s0] = 1
    
    # Find the first position where the character changes
    p = 1
    while p < N and s[p] == s0:
        p += 1
    
    # Determine the initial xor value
    xor = 0 if p % 2 == 0 else s0
    
    # Iterate over the rest of the string
    for (i, c) in enumerate(s[p:], start=p):
        d, e = c % 3 + 1, (c + 1) % 3 + 1
        dp[c] = sum(dp) % MOD
        dp[d], dp[e] = dp[e], dp[d]
        
        if i == p:
            dp[c] += p // 2
            dp[s[i - 1] ^ c] += (p - 1) // 2
        elif xor == 0:
            dp[c] += 1
        
        xor ^= c
    
    # Return the sum of dp array modulo MOD
    return sum(dp) % MOD
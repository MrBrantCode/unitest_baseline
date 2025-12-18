"""
QUESTION:
The chef is very expert in coding, so to keep his password safe from the hackers. He always enters a decoded code of his password. You are a hacker and your work is to find the maximum number of possible ways to unlock his password in encoded form.

The encoded message containing only letters from A-Z is being encoded with numbers using the following mapping: 

'A' -> 1 

'B' -> 2 ... 

'Z' -> 26

You have given a non-empty string containing only digits, determine the total number of ways to encode it. 

If the total number of ways are even then you are able to unlock the password. 

Input: 
The first line has a single integer T, denoting the number of test cases. The first line of each test case contains string “S” decoded number.

Output:
For each test case, in a new line, print 'YES' if number of maximum ways are even, otherwise
'NO'. (without quotes)

Constraints:
1 ≤ T ≤ 50

1 ≤ S ≤ 30

Sample Input:
2

12

223

Sample Output:
YES

NO

Explanation:
For first test case, It could be encoded as "AB" (1 2) or "L" (12), hence the number of
maximum possible ways are 2 so output is “YES”.
"""

def can_unlock_password(encoded_string: str) -> str:
    if not encoded_string:
        return 'NO'
    
    dp = [0] * (len(encoded_string) + 1)
    dp[0] = 1
    dp[1] = 1 if 0 < int(encoded_string[0]) <= 9 else 0
    
    for i in range(2, len(encoded_string) + 1):
        if 0 < int(encoded_string[i - 1:i]) <= 9:
            dp[i] += dp[i - 1]
        if encoded_string[i - 2:i][0] != '0' and int(encoded_string[i - 2:i]) <= 26:
            dp[i] += dp[i - 2]
    
    return 'YES' if dp[len(encoded_string)] % 2 == 0 else 'NO'
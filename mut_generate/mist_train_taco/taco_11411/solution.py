"""
QUESTION:
A newspaper is published in Walrusland. Its heading is s1, it consists of lowercase Latin letters. Fangy the little walrus wants to buy several such newspapers, cut out their headings, glue them one to another in order to get one big string. After that walrus erase several letters from this string in order to get a new word s2. It is considered that when Fangy erases some letter, there's no whitespace formed instead of the letter. That is, the string remains unbroken and it still only consists of lowercase Latin letters.

For example, the heading is "abc". If we take two such headings and glue them one to the other one, we get "abcabc". If we erase the letters on positions 1 and 5, we get a word "bcac".

Which least number of newspaper headings s1 will Fangy need to glue them, erase several letters and get word s2?

Input

The input data contain two lines. The first line contain the heading s1, the second line contains the word s2. The lines only consist of lowercase Latin letters (1 ≤ |s1| ≤ 104, 1 ≤ |s2| ≤ 106).

Output

If it is impossible to get the word s2 in the above-described manner, print "-1" (without the quotes). Otherwise, print the least number of newspaper headings s1, which Fangy will need to receive the word s2.

Examples

Input

abc
xyz


Output

-1


Input

abcd
dabc


Output

2
"""

import math

def minimum_headings_needed(s1: str, s2: str) -> int:
    na = len(s1)
    nb = len(s2)
    
    # Create a DP table to store the next occurrence of each character in s1
    dp = [[-1 for _ in range(26)] for _ in range(na + 1)]
    
    # Fill the DP table
    for i in range(na - 1, -1, -1):
        for j in range(26):
            dp[i][j] = dp[i + 1][j]
        dp[i][ord(s1[i]) - 97] = i
    
    cp = 0
    ans = 1
    i = 0
    
    while i < nb:
        if cp == na:
            ans += 1
            cp = 0
        if dp[cp][ord(s2[i]) - 97] == -1:
            ans += 1
            cp = 0
            if dp[cp][ord(s2[i]) - 97] == -1:
                ans = math.inf
                break
        cp = dp[cp][ord(s2[i]) - 97] + 1
        i += 1
    
    return ans if ans != math.inf else -1
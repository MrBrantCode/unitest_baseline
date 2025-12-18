"""
QUESTION:
Given a string t, we will call it unbalanced if and only if the length of t is at least 2, and more than half of the letters in t are the same. For example, both voodoo and melee are unbalanced, while neither noon nor a is.
You are given a string s consisting of lowercase letters. Determine if there exists a (contiguous) substring of s that is unbalanced. If the answer is positive, show a position where such a substring occurs in s.

-----Constraints-----
 - 2 ≦ |s| ≦ 10^5
 - s consists of lowercase letters.

-----Partial Score-----
 - 200 points will be awarded for passing the test set satisfying 2 ≦ N ≦ 100.

-----Input-----
The input is given from Standard Input in the following format:
s

-----Output-----
If there exists no unbalanced substring of s, print -1 -1.
If there exists an unbalanced substring of s, let one such substring be s_a s_{a+1} ... s_{b} (1 ≦ a < b ≦ |s|), and print a b. If there exists more than one such substring, any of them will be accepted.

-----Sample Input-----
needed

-----Sample Output-----
2 5

The string s_2 s_3 s_4 s_5 = eede is unbalanced. There are also other unbalanced substrings. For example, the output 2 6 will also be accepted.
"""

def find_unbalanced_substring(s: str) -> tuple:
    l = len(s)
    
    # Edge case: if the length of the string is 2
    if l == 2:
        if s[0] == s[1]:
            return (1, 2)
        else:
            return (-1, -1)
    
    # Check for unbalanced substrings of length 3
    for i in range(l - 2):
        s1 = s[i]
        s2 = s[i + 1]
        s3 = s[i + 2]
        if s1 == s2 or s1 == s3 or s2 == s3:
            return (i + 1, i + 3)
    
    # If no unbalanced substring is found
    return (-1, -1)
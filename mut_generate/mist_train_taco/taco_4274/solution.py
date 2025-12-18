"""
QUESTION:
For two strings A and B, we define the similarity of the strings to be the length of the longest prefix common to both strings. For example, the similarity of strings "abc" and "abd" is 2, while the similarity of strings "aaa" and "aaab" is 3.

Calculate the sum of similarities of a string S with each of it's suffixes.

Input Format

The first line contains the number of test cases t. 

Each of the next t lines contains a string to process, $\boldsymbol{\mathrm{~S~}}$.

Constraints

$1\leq t\leq10$    
$1\leq|s|\leq1000000$  
$\boldsymbol{\mathrm{~S~}}$ is composed of characters in the range ascii[a-z]  

Output Format

Output t lines, each containing the answer for the corresponding test case.

Sample Input
2
ababaa  
aa

Sample Output
11  
3

Explanation

For the first case, the suffixes of the string are "ababaa", "babaa", "abaa", "baa", "aa" and "a". The similarities of these strings with the string "ababaa" are 6,0,3,0,1, & 1 respectively. Thus, the answer is 6 + 0 + 3 + 0 + 1 + 1 = 11.

For the second case, the answer is 2 + 1 = 3.
"""

def calculate_similarity_sum(s: str) -> int:
    n = len(s)
    z = [0] * n
    l, r = 0, 0
    
    for i in range(1, n):
        if i <= r and z[i - l] < r - i + 1:
            z[i] = z[i - l]
        else:
            l = i
            if i > r:
                r = i
            while r < n and s[r - l] == s[r]:
                r += 1
            z[i] = r - l
            r -= 1
    
    return n + sum(z)
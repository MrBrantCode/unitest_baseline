"""
QUESTION:
Raj's lucky number is 101. His girl friend Rani  wants to give him a string S as a birthday present to him. She went to a shop and there are variety of strings which contains only 1 and 0 ( Binary string ) in that shop. Now in order to impress Raj , she wants to buy a string with highest number of subsequence’s of 101's . She needs your help. given a string S which contains only 1's and 0's , tell her the number of subsequence’s of 101 found in that string.

Input Format:

Only line of input file contains the string S

Output Format:

Print the result 

Constraints:

1 ≤ |S| ≤ 1000000

S[i] belongs to {0,1}

SAMPLE INPUT
10101

SAMPLE OUTPUT
4

Explanation

The indices of sequences containing 101 are : {0, 1, 2}, {2, 3, 4}, {0, 1, 4} and {0, 3, 4}.
"""

def count_subsequences_of_101(s: str) -> int:
    sub = '101'
    m, n = len(s), len(sub)
    table = [0] * n
    
    for i in range(m):
        previous = 1
        for j in range(n):
            current = table[j]
            if s[i] == sub[j]:
                table[j] += previous
            previous = current
    
    return table[n-1] if n else 1
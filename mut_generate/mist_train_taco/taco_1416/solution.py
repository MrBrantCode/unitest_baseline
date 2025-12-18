"""
QUESTION:
You are given two strings s and t consisting of lowercase Latin letters. The length of t is 2 (i.e. this string consists only of two characters).

In one move, you can choose any character of s and replace it with any lowercase Latin letter. More formally, you choose some i and replace s_i (the character at the position i) with some character from 'a' to 'z'.

You want to do no more than k replacements in such a way that maximizes the number of occurrences of t in s as a subsequence.

Recall that a subsequence is a sequence that can be derived from the given sequence by deleting zero or more elements without changing the order of the remaining elements.

Input

The first line of the input contains two integers n and k (2 ≤ n ≤ 200; 0 ≤ k ≤ n) — the length of s and the maximum number of moves you can make. The second line of the input contains the string s consisting of n lowercase Latin letters. The third line of the input contains the string t consisting of two lowercase Latin letters.

Output

Print one integer — the maximum possible number of occurrences of t in s as a subsequence if you replace no more than k characters in s optimally.

Examples

Input


4 2
bbaa
ab


Output


3


Input


7 3
asddsaf
sd


Output


10


Input


15 6
qwertyhgfdsazxc
qa


Output


16


Input


7 2
abacaba
aa


Output


15

Note

In the first example, you can obtain the string "abab" replacing s_1 with 'a' and s_4 with 'b'. Then the answer is 3.

In the second example, you can obtain the string "ssddsdd" and get the answer 10.

In the fourth example, you can obtain the string "aaacaaa" and get the answer 15.
"""

def maximize_subsequence_occurrences(n, k, s, t):
    a, b = t[0], t[1]
    
    if a == b:
        x = min(s.count(a) + k, n)
        return x * (x - 1) // 2
    else:
        dp = [[-10000] * (k + 2) for _ in range(n + 2)]
        dp[1][1] = 0
        
        for i in range(n):
            for q in range(i + 2, 0, -1):
                for t in range(min(k, i + 1) + 1, 0, -1):
                    dp[q][t] = max(dp[q][t], dp[q - 1][t - (0 if s[i] == a else 1)], dp[q][t - (0 if s[i] == b else 1)] + q - 1)
        
        return max(i for line in dp for i in line)
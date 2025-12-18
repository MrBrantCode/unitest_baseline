"""
QUESTION:
A bracket sequence is a string containing only characters "(" and ")". A regular bracket sequence (or, shortly, an RBS) is a bracket sequence that can be transformed into a correct arithmetic expression by inserting characters "1" and "+" between the original characters of the sequence. For example:

  * bracket sequences "()()" and "(())" are regular (the resulting expressions are: "(1)+(1)" and "((1+1)+1)"); 
  * bracket sequences ")(", "(" and ")" are not. 



Let's denote the concatenation of two strings x and y as x+y. For example, "()()" + ")(" = "()())(".

You are given n bracket sequences s_1, s_2, ..., s_n. You can rearrange them in any order (you can rearrange only the strings themselves, but not the characters in them).

Your task is to rearrange the strings in such a way that the string s_1 + s_2 + ... + s_n has as many non-empty prefixes that are RBS as possible.

Input

The first line contains a single integer n (1 ≤ n ≤ 20).

Then n lines follow, the i-th of them contains s_i — a bracket sequence (a string consisting of characters "(" and/or ")". All sequences s_i are non-empty, their total length does not exceed 4 ⋅ 10^5.

Output

Print one integer — the maximum number of non-empty prefixes that are RBS for the string s_1 + s_2 + ... + s_n, if the strings s_1, s_2, ..., s_n can be rearranged arbitrarily.

Examples

Input


2
(
)


Output


1


Input


4
()()())
(
(
)


Output


4


Input


1
(())


Output


1


Input


1
)(()


Output


0

Note

In the first example, you can concatenate the strings as follows: "(" + ")" = "()", the resulting string will have one prefix, that is an RBS: "()".

In the second example, you can concatenate the strings as follows: "(" + ")" + "()()())" + "(" = "()()()())(", the resulting string will have four prefixes that are RBS: "()", "()()", "()()()", "()()()()".

The third and the fourth examples contain only one string each, so the order is fixed.
"""

def max_rbs_prefixes(n, sequences):
    smin = [0] * n
    smnum = [0] * n
    h = [0] * n
    cnts = [{} for _ in range(n)]
    
    for i in range(n):
        ts = sequences[i]
        nmin = 0
        nh = 0
        for c in ts:
            if c == '(':
                nh += 1
            else:
                nh -= 1
            if smin[i] > nh:
                smin[i] = nh
                smnum[i] = 0
            if smin[i] == nh:
                smnum[i] += 1
            if nh == smin[i]:
                if nh not in cnts[i]:
                    cnts[i][nh] = 0
                cnts[i][nh] += 1
        h[i] = nh
    
    dp = [float('-inf')] * 2 ** n
    dp[0] = 0
    ans = 0
    
    for i in range(2 ** n):
        nh = 0
        for j in range(n):
            if 2 ** j & i > 0:
                nh += h[j]
        for j in range(n):
            if 2 ** j & i == 0 and nh + smin[j] >= 0:
                if nh + smin[j] == 0:
                    dp[2 ** j | i] = max(dp[2 ** j | i], dp[i] + smnum[j])
                else:
                    dp[2 ** j | i] = max(dp[2 ** j | i], dp[i])
            elif 2 ** j & i == 0 and -1 * nh in cnts[j]:
                ans = max(ans, dp[i] + cnts[j][-1 * nh])
    
    ans = max(ans, max(dp))
    return ans
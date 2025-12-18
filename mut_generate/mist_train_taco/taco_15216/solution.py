"""
QUESTION:
Tavas is a strange creature. Usually "zzz" comes out of people's mouth while sleeping, but string s of length n comes out from Tavas' mouth instead.

<image>

Today Tavas fell asleep in Malekas' place. While he was sleeping, Malekas did a little process on s. Malekas has a favorite string p. He determined all positions x1 < x2 < ... < xk where p matches s. More formally, for each xi (1 ≤ i ≤ k) he condition sxisxi + 1... sxi + |p| - 1 = p is fullfilled.

Then Malekas wrote down one of subsequences of x1, x2, ... xk (possibly, he didn't write anything) on a piece of paper. Here a sequence b is a subsequence of sequence a if and only if we can turn a into b by removing some of its elements (maybe no one of them or all).

After Tavas woke up, Malekas told him everything. He couldn't remember string s, but he knew that both p and s only contains lowercase English letters and also he had the subsequence he had written on that piece of paper.

Tavas wonders, what is the number of possible values of s? He asked SaDDas, but he wasn't smart enough to solve this. So, Tavas asked you to calculate this number for him.

Answer can be very large, so Tavas wants you to print the answer modulo 109 + 7.

Input

The first line contains two integers n and m, the length of s and the length of the subsequence Malekas wrote down (1 ≤ n ≤ 106 and 0 ≤ m ≤ n - |p| + 1).

The second line contains string p (1 ≤ |p| ≤ n).

The next line contains m space separated integers y1, y2, ..., ym, Malekas' subsequence (1 ≤ y1 < y2 < ... < ym ≤ n - |p| + 1).

Output

In a single line print the answer modulo 1000 000 007.

Examples

Input

6 2
ioi
1 3


Output

26


Input

5 2
ioi
1 2


Output

0

Note

In the first sample test all strings of form "ioioi?" where the question mark replaces arbitrary English letter satisfy.

Here |x| denotes the length of string x.

Please note that it's possible that there is no such string (answer is 0).
"""

def calculate_possible_strings(n, m, p, subsequence):
    MOD = 10**9 + 7
    
    def matching(s):
        le = len(s)
        pi = [0] * le
        for i in range(1, le):
            j = pi[i - 1]
            while j > 0 and s[i] != s[j]:
                j = pi[j - 1]
            if s[i] == s[j]:
                j += 1
            pi[i] = j
        w = set()
        i = le - 1
        while pi[i] != 0:
            w.add(le - pi[i])
            i = pi[i] - 1
        return w
    
    if m == 0:
        return pow(26, n, MOD)
    
    l = len(p)
    pre = matching(p)
    filled = l
    
    for i in range(1, m):
        if subsequence[i] - subsequence[i - 1] < l and subsequence[i] - subsequence[i - 1] not in pre:
            return 0
        filled += min(l, subsequence[i] - subsequence[i - 1])
    
    return pow(26, n - filled, MOD)
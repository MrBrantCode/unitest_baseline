"""
QUESTION:
This is the hard version of the problem. The difference is the constraint on the sum of lengths of strings and the number of test cases. You can make hacks only if you solve all versions of this task.

You are given a string $s$, consisting of lowercase English letters. Find the longest string, $t$, which satisfies the following conditions:   The length of $t$ does not exceed the length of $s$.  $t$ is a palindrome.  There exists two strings $a$ and $b$ (possibly empty), such that $t = a + b$ ( "$+$" represents concatenation), and $a$ is prefix of $s$ while $b$ is suffix of $s$. 


-----Input-----

The input consists of multiple test cases. The first line contains a single integer $t$ ($1 \leq t \leq 10^5$), the number of test cases. The next $t$ lines each describe a test case.

Each test case is a non-empty string $s$, consisting of lowercase English letters.

It is guaranteed that the sum of lengths of strings over all test cases does not exceed $10^6$.


-----Output-----

For each test case, print the longest string which satisfies the conditions described above. If there exists multiple possible solutions, print any of them.


-----Example-----
Input
5
a
abcdfdcecba
abbaxyzyx
codeforces
acbba

Output
a
abcdfdcba
xyzyx
c
abba



-----Note-----

In the first test, the string $s = $"a" satisfies all conditions.

In the second test, the string "abcdfdcba" satisfies all conditions, because:  Its length is $9$, which does not exceed the length of the string $s$, which equals $11$.  It is a palindrome.  "abcdfdcba" $=$ "abcdfdc" $+$ "ba", and "abcdfdc" is a prefix of $s$ while "ba" is a suffix of $s$. 

It can be proven that there does not exist a longer string which satisfies the conditions.

In the fourth test, the string "c" is correct, because "c" $=$ "c" $+$ "" and $a$ or $b$ can be empty. The other possible solution for this test is "s".
"""

def find_longest_palindrome_prefix_suffix(s: str) -> str:
    def manacher(S):
        N = len(S)
        (r, p) = (0, 0)
        A = [0] * N
        for i in range(N):
            if i <= r:
                A[i] = min(A[2 * p - i], r - i)
            else:
                A[i] = 0
            while i - A[i] - 1 >= 0 and i + A[i] + 1 < N and (S[i - A[i] - 1] == S[i + A[i] + 1]):
                A[i] += 1
            if r < i + A[i]:
                r = i + A[i]
                p = i
        return A

    def f(S):
        return ''.join([i for i in S if i != '#'])

    n = len(s)
    if n % 2 == 0:
        c = ''
        v = s[:n // 2]
    else:
        c = s[n // 2]
        v = s[:n // 2]

    for i in range(n // 2):
        if s[i] != s[n - 1 - i]:
            c = s[i:n - i]
            v = s[:i]
            break

    a = '#'.join(c)
    a = '#' + a + '#'
    A = manacher(a)

    ans1 = ''
    for i in range(len(c), 0, -1):
        if i == A[i]:
            ans1 = a[:i * 2]
            break
    ans1 = f(ans1)

    ans2 = ''
    for i in range(len(c), 0, -1):
        if i == A[-1 - i]:
            ans2 = a[-i * 2 - 1:]
            break
    ans2 = f(ans2)

    if len(ans1) > len(ans2):
        ans = ans1
    else:
        ans = ans2

    return v + ans + v[::-1]
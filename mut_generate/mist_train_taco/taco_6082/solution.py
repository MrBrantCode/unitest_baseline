"""
QUESTION:
Marina loves strings of the same length and Vasya loves when there is a third string, different from them in exactly t characters. Help Vasya find at least one such string.

More formally, you are given two strings s_1, s_2 of length n and number t. Let's denote as f(a, b) the number of characters in which strings a and b are different. Then your task will be to find any string s_3 of length n, such that f(s_1, s_3) = f(s_2, s_3) = t. If there is no such string, print  - 1.


-----Input-----

The first line contains two integers n and t (1 ≤ n ≤ 10^5, 0 ≤ t ≤ n).

The second line contains string s_1 of length n, consisting of lowercase English letters.

The third line contain string s_2 of length n, consisting of lowercase English letters.


-----Output-----

Print a string of length n, differing from string s_1 and from s_2 in exactly t characters. Your string should consist only from lowercase English letters. If such string doesn't exist, print -1.


-----Examples-----
Input
3 2
abc
xyc

Output
ayd
Input
1 0
c
b

Output
-1
"""

def find_third_string(n, t, s1, s2):
    common = 0
    diff = 0
    for i in range(n):
        if s1[i] == s2[i]:
            common += 1
        else:
            diff += 1
    
    chars = 'abcdefghijklmnopqrstuvwxyz'
    ans = []
    
    if common >= n - t:
        unc_common = n - t
        for i in range(n):
            if s1[i] == s2[i] and unc_common > 0:
                ans.append(s1[i])
                unc_common -= 1
            else:
                for char in chars:
                    if char != s1[i] and char != s2[i]:
                        ans.append(char)
                        break
        return ''.join(ans)
    else:
        unch = n - t - common
        unch1 = 0
        unch2 = 0
        if 2 * unch <= diff:
            for i in range(n):
                if s1[i] == s2[i]:
                    ans.append(s1[i])
                elif unch1 < unch:
                    ans.append(s1[i])
                    unch1 += 1
                elif unch2 < unch:
                    ans.append(s2[i])
                    unch2 += 1
                else:
                    for char in chars:
                        if char != s1[i] and char != s2[i]:
                            ans.append(char)
                            break
            return ''.join(ans)
        else:
            return -1
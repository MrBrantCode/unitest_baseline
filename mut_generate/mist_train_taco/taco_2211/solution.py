"""
QUESTION:
You are given a non-empty string s consisting of lowercase English letters. You have to pick exactly one non-empty substring of s and shift all its letters 'z' <image> 'y' <image> 'x' <image> 'b' <image> 'a' <image> 'z'. In other words, each character is replaced with the previous character of English alphabet and 'a' is replaced with 'z'.

What is the lexicographically minimum string that can be obtained from s by performing this shift exactly once?

Input

The only line of the input contains the string s (1 ≤ |s| ≤ 100 000) consisting of lowercase English letters.

Output

Print the lexicographically minimum string that can be obtained from s by shifting letters of exactly one non-empty substring.

Examples

Input

codeforces


Output

bncdenqbdr


Input

abacaba


Output

aaacaba

Note

String s is lexicographically smaller than some other string t of the same length if there exists some 1 ≤ i ≤ |s|, such that s1 = t1, s2 = t2, ..., si - 1 = ti - 1, and si < ti.
"""

def lexicographically_minimum_shift(s: str) -> str:
    l = len(s)
    a1 = a2 = 1000000
    q = []
    k = 0
    b = ''
    j = 0
    
    if 'a' in s:
        for i in s:
            if i == 'a':
                if len(q) > 0 and j - q[-1] > 1:
                    q.append(j)
                    k = j
                    break
                q.append(j)
            j += 1
        
        if len(q) == l:
            return 'a' * (l - 1) + 'z'
        
        if q[0] > 0:
            for i in range(0, q[0]):
                b += chr(ord(s[i]) - 1)
            b += s[q[0]:]
            return b
        
        if len(q) == 1:
            b += 'a'
            for i in range(1, l):
                b += chr(ord(s[i]) - 1)
        else:
            if s[:q[len(q) - 1] + 1] == 'a' * len(q):
                b += 'a' * len(q)
                for i in range(q[len(q) - 1] + 1, l):
                    b += chr(ord(s[i]) - 1)
                return b
            else:
                b += s[:q[len(q) - 2] + 1]
            for i in range(q[len(q) - 2] + 1, k):
                b += chr(ord(s[i]) - 1)
            if len(q) > 1:
                b += s[k:]
        return b
    else:
        for i in range(l):
            b += chr(ord(s[i]) - 1)
        return b
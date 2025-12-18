"""
QUESTION:
Mr. Takahashi has a string s consisting of lowercase English letters. He repeats the following operation on s exactly K times.

* Choose an arbitrary letter on s and change that letter to the next alphabet. Note that the next letter of `z` is `a`.



For example, if you perform an operation for the second letter on `aaz`, `aaz` becomes `abz`. If you then perform an operation for the third letter on `abz`, `abz` becomes `aba`.

Mr. Takahashi wants to have the lexicographically smallest string after performing exactly K operations on s. Find the such string.

Constraints

* 1≤|s|≤10^5
* All letters in s are lowercase English letters.
* 1≤K≤10^9

Input

The input is given from Standard Input in the following format:


s
K


Output

Print the lexicographically smallest string after performing exactly K operations on s.

Examples

Input

xyz
4


Output

aya


Input

a
25


Output

z


Input

codefestival
100


Output

aaaafeaaivap
"""

def smallest_string_after_operations(s: str, K: int) -> str:
    def dist(c: str) -> int:
        return (ord('z') - ord(c) + 1) % 26
    
    s = list(s)
    i = 0
    
    while 0 < K and i < len(s):
        d = dist(s[i])
        if d <= K:
            K -= d
            s[i] = 'a'
        i += 1
    
    s[-1] = chr(ord(s[-1]) + K % 26)
    
    return ''.join(s)
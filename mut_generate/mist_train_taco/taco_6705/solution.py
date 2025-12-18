"""
QUESTION:
Snuke has N strings. The i-th string is s_i.

Let us concatenate these strings into one string after arranging them in some order. Find the maximum possible number of occurrences of `AB` in the resulting string.

Constraints

* 1 \leq N \leq 10^{4}
* 2 \leq |s_i| \leq 10
* s_i consists of uppercase English letters.

Input

Input is given from Standard Input in the following format:


N
s_1
\vdots
s_N


Output

Print the answer.

Examples

Input

3
ABCA
XBAZ
BAD


Output

2


Input

9
BEWPVCRWH
ZZNQYIJX
BAVREA
PA
HJMYITEOX
BCJHMRMNK
BP
QVFABZ
PRGKSPUNA


Output

4


Input

7
RABYBBE
JOZ
BMHQUVA
BPA
ISU
MCMABAOBHZ
SZMEHMA


Output

4
"""

def max_ab_occurrences(N, strings):
    a = 0
    b = 0
    ab = 0
    cnt = 0
    
    for s in strings:
        tmp = re.findall('AB', s)
        ab += len(tmp)
        if s[0] == 'B':
            b += 1
        if s[-1] == 'A':
            a += 1
        if s[0] == 'B' and s[-1] == 'A':
            cnt += 1
    
    if a == b and a == cnt and (a > 0):
        return a - 1 + ab
    else:
        return min(a, b) + ab
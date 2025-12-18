"""
QUESTION:
Read problem statements in [Bengali], [Mandarin Chinese], [Russian], and [Vietnamese] as well.

You are given a binary string $S$. Chef defines $\mathrm{MEX}(S)$ as the smallest non-negative integer such that its binary representation (without leading '0'-s; in particular, the binary representation of $0$ is "0") is not a [subsequence] of $S$.

Chef is asking you to find $\mathrm{MEX}(S)$. Since this integer could be very large, find its binary representation (without leading '0'-s).

------  Input ------
The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
The first and only line of each test case contains a single string $S$.

------  Output ------
For each test case, print a single line containing one string: $\mathrm{MEX}(S)$ in binary representation.

------  Constraints ------
$1 ≤ T ≤ 10^{5}$
$1 ≤ |S| ≤ 10^{6}$
$S$ contains only characters '0' and '1'
the sum of $|S|$ over all test cases does not exceed $2 \cdot 10^{6}$

------  Subtasks ------
Subtask #1 (20 points): 
- $1 ≤ T ≤  2 \cdot 10^{3}$
$|S| ≤ 10$

Subtask #2 (20 points): 
- $1 ≤ T ≤  10^{5}$
$|S| ≤ 60$

Subtask #2 (60 points):
- original constraints

----- Sample Input 1 ------ 
2

1001011

1111
----- Sample Output 1 ------ 
1100

0
----- explanation 1 ------ 
Example case 1: All integers between $0$ and $11$ inclusive, in binary representation, appear in $S$ as subsequences. However, the binary representation of $12$ (which is "1100") is not a subsequence of $S$.

Example case 2: Since $S$ contains only '1'-s, the string "0" is not a subsequence of $S$ and therefore $\mathrm{MEX}(S) = 0$.
"""

def find_mex_binary(S: str) -> str:
    l = len(S)
    next0 = [-1] * l
    next1 = [-1] * l
    lens = [0] * l
    j = l - 1
    z = o = 0
    c = 1
    n0 = -1
    n1 = -1
    
    while j >= 0:
        lens[j] = c
        next0[j] = n0
        next1[j] = n1
        if S[j] == '0':
            z = 1
            n0 = j
        else:
            o = 1
            n1 = j
        if z == 1 and o == 1:
            c += 1
            z = o = 0
        j -= 1
    
    if n0 == -1:
        return '0'
    if n1 == -1:
        return '1'
    
    result = ''
    j = n1
    while True:
        result += S[j]
        if next0[j] == -1:
            result += '0'
            break
        elif next1[j] == -1:
            result += '1'
            break
        elif lens[next0[j]] <= lens[next1[j]]:
            j = next0[j]
        else:
            j = next1[j]
    
    return result
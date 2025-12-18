"""
QUESTION:
Chef has a binary string S. He can modify it by choosing any subsequence of length 3 from it and deleting the first and last character of the subsequence.

For example, if S = \textcolor{red}{11}01\textcolor{red}{0}1, Chef can choose the subsequence marked in red and delete its first and last characters, obtaining the string S = 1011.

Chef wonders what is the lexicographically largest string he can obtain by modifying the original string using a finite number of operations. Please help Chef in this task.

Note: A binary string A is said to be lexicographically larger than another binary string B if:
B is a proper prefix of A (for example, 101 is lexicographically larger than 10); or
There exists an index i such that A_{1} = B_{1}, A_{2} = B_{2}, \ldots, A_{i-1} = B_{i-1} and A_{i} > B_{i}.

------ Input Format ------ 

- The first line of input will contain a single integer T, denoting the number of test cases.
- Each test case consists of a single line of input containing the original binary string S.

------ Output Format ------ 

For each test case, output on a new line the lexicographically largest string Chef can obtain.

------ Constraints ------ 

$1 ≤ T ≤ 2\cdot 10^{4}$
$3 ≤ |S| ≤ 10^{5}$
$S$ is a binary string, i.e, only contains the characters $0$ and $1$ in it
- The sum of $|S|$ over all test cases won't exceed $3\cdot 10^{5}$.

----- Sample Input 1 ------ 
4
101
1010
0000
0001

----- Sample Output 1 ------ 
101
11
0000
01

----- explanation 1 ------ 
Test case $1$: It is optimal to not perform any moves.

Test case $2$: In one move, by choosing the subsequence $1\textcolor{red}{010}$, the string can be made into $11$, which is the lexicographically largest possible.

Test case $3$: It is optimal to not perform any move.
"""

def largest_lexicographical_binary_string(S: str) -> str:
    if '1' not in S:
        return S
    
    k = S.rfind('1')
    suf = S[k:]
    S = S[:k]
    k = S.count('0')
    
    if k & 1:
        if '0' in suf:
            return S.replace('0', '') + suf[:-1]
        elif S[-1] == '1':
            return S.replace('0', '')
        elif S[-2] == '0':
            return S.replace('0', '') + '01'
        elif S.rfind('0', 0, -1) - S.find('0') + 1 != k - 1:
            return S.replace('0', '') + '01'
        else:
            return S.replace('0', '')
    elif S.rfind('0') - S.find('0') + 1 != k:
        return S.replace('0', '') + suf
    elif len(suf) >= 3:
        return S.replace('0', '') + suf[:-2]
    elif len(suf) == 2:
        if S[-1] == '1':
            return S.replace('0', '')
        else:
            return S.replace('0', '') + '01'
    elif S.endswith('11'):
        return S.replace('0', '')[:-1]
    elif S[-1] == '1':
        return S.replace('0', '')[:-1] + '01'
    else:
        return S.replace('0', '') + '001'
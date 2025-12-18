"""
QUESTION:
Chef has a binary string S of length N. Chef wants to find two disjoint substrings of equal length, such that their [bitwise XOR] is maximised.

Formally, Chef wants to find L_{1}, R_{1}, L_{2}, and R_{2} such that:
1 ≤ L_{1} ≤ R_{1} < L_{2} ≤ R_{2} ≤ N, that is, the substrings are disjoint (have no common elements);
|R_{1} - L_{1} + 1| = |R_{2} - L_{2} + 1|, that is, the substrings have equal length;
S_{L_{1} \dots R_{1}} \oplus S_{L_{2} \dots R_{2}} is maximised, where \oplus is the bitwise XOR operation.

Output the maximum XOR value in decimal notation. Since the value can be large, output it module 10^{9}+7.

Note that a substring is formed by deleting some (possibly zero) characters from the beginning and some (possibly zero) characters from the end of the string.

------ Input Format ------ 

- The first line of input will contain a single integer T, denoting the number of test cases.
- Each test case consists of multiple lines of input.
- The first line of each test case contains a single integer N denoting the length of string S.
- The second line of each test case contains a binary string S of length N containing 0s and 1s only.

------ Output Format ------ 

For each test case, output the maximum XOR value in decimal notation. Since the value can be large, output it module 10^{9}+7.

------ Constraints ------ 

$1 ≤ T ≤ 10^{5}$
$2 ≤ N ≤ 5000$
$S$ contains $0$ and $1$ only.
- The sum of $N^{2}$ over all test cases won't exceed $2.5 \cdot 10^{7}$.

----- Sample Input 1 ------ 
3
4
1001
5
11111
3
011

----- Sample Output 1 ------ 
3
0
1

----- explanation 1 ------ 
Test case $1$: We can choose $L_{1} = 1, R_{1} = 2, L_{2} = 3,$ and $R_{2} = 4$. Thus, the chosen substrings are $10$ and $01$. The XOR of these substrings is $11$ whose decimal equivalent is $3$.

Test case $2$: We can choose $L_{1} = 2, R_{1} = 2, L_{2} = 4,$ and $R_{2} = 4$. Thus, the chosen substrings are $1$ and $1$. The XOR of these substrings is $0$ whose decimal equivalent is $0$.

Test case $3$: We can choose $L_{1} = 1, R_{1} = 1, L_{2} = 3,$ and $R_{2} = 3$. Thus, the chosen substrings are $0$ and $1$. The XOR of these substrings is $1$ whose decimal equivalent is $1$.
"""

def max_xor_of_disjoint_substrings(S, N):
    mo = 1000000007
    z = []
    o = []
    
    # Separate indices of '0's and '1's
    for i in range(N):
        if S[i] == '0':
            z.append(i)
        else:
            o.append(i)
    
    # Determine the maximum length of substrings to consider
    for l in range(N // 2, 0, -1):
        flag = False
        for s in range(N - 2 * l + 1):
            if S[s] == '0':
                ind = bisect_left(o, s + l)
                if ind != len(o) and o[ind] <= N - l:
                    flag = True
                    break
            else:
                ind = bisect_left(z, s + l)
                if ind != len(z) and z[ind] <= N - l:
                    flag = True
                    break
        if flag:
            break
    else:
        return 0
    
    # Find the maximum XOR value for substrings of length l
    ans = '0' * l
    for s in range(N - 2 * l + 1):
        for e in range(s + l, N - l + 1):
            if S[s] != S[e]:
                tans = ''
                for i in range(l):
                    if S[s + i] != S[e + i]:
                        tans += '1'
                    else:
                        tans += '0'
                if tans > ans:
                    ans = tans
    
    # Convert the binary string to decimal and take modulo 10^9 + 7
    nu = 0
    for i in range(l):
        nu *= 2
        nu += ord(ans[i]) - ord('0')
        nu %= mo
    
    return nu
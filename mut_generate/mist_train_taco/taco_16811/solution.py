"""
QUESTION:
Reyaan has given you the following problem to solve:

You are given an integer K in base B, represented by an array A of length N such that
0 ≤ A_{i} < B for every 1 ≤ i ≤ N
\sum_{i=1}^N A_{i} \cdot B^{N-i} = K

Note that N ≤ B in this problem.

Find the smallest non-negative integer X such that X+K contains *every* digit from 0 to B-1 in its base-B representation.

X can be very large, so print the answer modulo 10^{9} + 7.

Note: Leading zeros are not counted as part of the number, so for example 12 = 012 has only two distinct digits: 1 and 2. However, 102 does have three distinct digits.

------ Input Format ------ 

- The first line of input will contain a single integer T, denoting the number of test cases.
- Each test case consists of two lines of input.
- The first line of each test case contains two space-separated integers N and B — the size of the array A and the base.
- The second line of each test case contains N space-separated integers A_{1}, A_{2}, \ldots, A_{N}.

------ Output Format ------ 

For each test case, output on a new line the value of X, modulo 10^{9} + 7.

------ Constraints ------ 

$1 ≤ T ≤ 10^{4}$
$1 ≤ N ≤ 10^{6}$
$2 ≤ B ≤ 10^{6}$
$N ≤ B$
$0 ≤ A_{i} < B$
$A_{1} > 0$, i.e, the given number doesn't contain leading zeros.
- The sum of $B$ across all test cases won't exceed $10^{6}$.

----- Sample Input 1 ------ 
4
4 4
3 1 0 2
4 5
1 2 3 4
2 2
1 1
1 3
2

----- Sample Output 1 ------ 
0
500
1
9

----- explanation 1 ------ 
Test case $1$: All the digits from $0$ to $B-1=3$ are already present in the given array, so $X = 0$.

Test case $2$: In base $5$, $[1, 2, 3, 4]$ represents the integer $194$. The smallest number larger than the given one that contains every digit is $[1, 0, 2, 3, 4]$, which represents
$694$. The difference between them is $500$.

Test case $3$: We have $K = 3$, which is $[1, 1]$ in binary. If we add $X = 1$ to it, we obtain $K+X = 4$, which is $[1, 0, 0]$ in binary and has both digits.
"""

def itable_to_multiset(s):
    rv = {}
    for x in s:
        rv[x] = rv.get(x, 0) + 1
    return rv

def answer(b, finish, start, m):
    assert len(start) == len(finish)
    rv = 0
    for (s, f) in zip(start, finish):
        rv *= b
        rv %= m
        rv += f - s
    return rv % m

def find_smallest_x(n, b, A, modulus=10**9 + 7):
    dig_freqs = itable_to_multiset(A)
    all_digs = set(range(b))
    missing = all_digs - set(dig_freqs.keys())
    
    if len(missing) == 0:
        return 0
    
    done = False
    max_missing = max(missing)
    
    for (dig, idx) in zip(reversed(A), range(1, n + 1)):
        dig_freqs[dig] -= 1
        if dig_freqs[dig] == 0:
            missing.add(dig)
            if dig > max_missing:
                max_missing = dig
        
        if len(missing) > idx or dig == b - 1 or (len(missing) == idx and dig >= max_missing):
            continue
        
        if len(missing) < idx:
            new_dig = dig + 1
        else:
            new_dig = min(missing.intersection(range(dig + 1, b)))
        
        if new_dig in missing:
            missing.remove(new_dig)
        
        missing = list(missing)
        missing.sort()
        
        return answer(b, [new_dig] + [0] * (idx - 1 - len(missing)) + missing, A[-idx:], modulus)
    
    ans_len = max(n + 1, b)
    return answer(b, [1] + [0] * (ans_len + 1 - b) + list(range(2, b)), [0] * (ans_len - n) + A, modulus)
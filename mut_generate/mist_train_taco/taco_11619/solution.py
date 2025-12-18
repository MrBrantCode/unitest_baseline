"""
QUESTION:
Problem

Given a permutation of length $ N $ $ P = \\ {P_1, P_2, \ ldots, P_N \\} $ and the integer $ K $.
Determine if the permutation $ P $ can be monotonically increased by repeating the following operation any number of times $ 0 $ or more.

* Choose the integer $ x \ (0 \ le x \ le N-K) $. Patrol right shift around $ P_ {x + 1}, \ ldots, P_ {x + K} $



However, the cyclic right shift of the subsequence $ U = U_1, \ ldots, U_M $ means that $ U = U_1, \ ldots, U_M $ is changed to $ U = U_M, U_1, \ ldots, U_ {M-1} $. Means to change.

Constraints

The input satisfies the following conditions.

* $ 2 \ leq K \ leq N \ leq 10 ^ 5 $
* $ 1 \ leq P_i \ leq N \ (1 \ leq i \ leq N) $
* $ P_i \ neq P_j \ (i \ neq j) $
* All inputs are integers

Input

The input is given in the following format.


$ N $ $ K $
$ P_1 $ $ \ ldots $ $ P_N $


Permutation length $ N $ and integer $ K $ are given in the first row, separated by blanks.
The elements of the permutation $ P $ are given in the second row, separated by blanks.

Output

Print "Yes" if you can monotonically increase $ P $, otherwise print "No" on the $ 1 $ line.

Examples

Input

3 3
2 3 1


Output

Yes


Input

3 2
1 2 3


Output

Yes


Input

3 3
3 2 1


Output

No
"""

def can_be_monotonically_increased(N, K, P):
    def add(i, bit):
        while i <= N:
            bit[i] += 1
            i += i & -i

    def sum(i, bit):
        res = 0
        while i > 0:
            res += bit[i]
            i -= i & -i
        return res

    if N > K:
        if K % 2 == 0:
            return 'Yes'
        else:
            a = 0
            bit = [0] * (N + 1)
            for i in range(N):
                a ^= i - sum(P[i], bit) & 1
                add(P[i], bit)
            if a:
                return 'No'
            else:
                return 'Yes'
    else:
        for i in range(N):
            if P[i] == 1:
                break
        for j in range(N):
            if P[(j + i) % N] != j + 1:
                return 'No'
        return 'Yes'
"""
QUESTION:
There is a set consisting of N distinct integers. The i-th smallest element in this set is S_i. We want to divide this set into two sets, X and Y, such that:

* The absolute difference of any two distinct elements in X is A or greater.
* The absolute difference of any two distinct elements in Y is B or greater.



How many ways are there to perform such division, modulo 10^9 + 7? Note that one of X and Y may be empty.

Constraints

* All input values are integers.
* 1 ≦ N ≦ 10^5
* 1 ≦ A , B ≦ 10^{18}
* 0 ≦ S_i ≦ 10^{18}(1 ≦ i ≦ N)
* S_i < S_{i+1}(1 ≦ i ≦ N - 1)

Input

The input is given from Standard Input in the following format:


N A B
S_1
:
S_N


Output

Print the number of the different divisions under the conditions, modulo 10^9 + 7.

Examples

Input

5 3 7
1
3
6
9
12


Output

5


Input

7 5 3
0
2
4
7
8
11
15


Output

4


Input

8 2 9
3
4
5
13
15
22
26
32


Output

13


Input

3 3 4
5
6
7


Output

0
"""

def count_divisions(N, A, B, S):
    from bisect import bisect_right
    INF = 10 ** 18 + 100
    MOD = 10 ** 9 + 7
    
    S = [-INF] + S  # Add a sentinel value to handle edge cases
    dpX = [0] * (N + 1)
    dpY = [0] * (N + 1)
    dpX[0] = 1
    dpY[0] = 1
    dpX_cum = [1] * (N + 1) + [0]
    dpY_cum = [1] * (N + 1) + [0]
    dpX_left = 0
    dpY_left = 0
    
    for n, x in enumerate(S[2:], 2):
        iA = bisect_right(S, x - A)
        iB = bisect_right(S, x - B)
        
        xy = dpY_cum[iB - 1] - dpY_cum[dpY_left - 1] if iB >= dpY_left else 0
        yx = dpX_cum[iA - 1] - dpX_cum[dpX_left - 1] if iA >= dpX_left else 0
        
        if iA != n:
            dpY_left = n - 1
        if iB != n:
            dpX_left = n - 1
        
        dpX[n - 1] = xy
        dpX_cum[n - 1] = (dpX_cum[n - 2] + xy) % MOD
        dpX_cum[n] = dpX_cum[n - 1]
        
        dpY[n - 1] = yx
        dpY_cum[n - 1] = (dpY_cum[n - 2] + yx) % MOD
        dpY_cum[n] = dpY_cum[n - 1]
    
    answer = dpX_cum[N - 1] - dpX_cum[dpX_left - 1]
    answer += dpY_cum[N - 1] - dpY_cum[dpY_left - 1]
    answer %= MOD
    
    return answer
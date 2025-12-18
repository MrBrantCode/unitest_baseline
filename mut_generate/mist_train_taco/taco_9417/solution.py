"""
QUESTION:
Given is a permutation P of \{1, 2, \ldots, N\}.
For a pair (L, R) (1 \le L \lt R \le N), let X_{L, R} be the second largest value among P_L, P_{L+1}, \ldots, P_R.
Find \displaystyle \sum_{L=1}^{N-1} \sum_{R=L+1}^{N} X_{L,R}.

-----Constraints-----
 -  2 \le N \le 10^5 
 -  1 \le P_i \le N 
 -  P_i \neq P_j  (i \neq j)
 - All values in input are integers.

-----Input-----
Input is given from Standard Input in the following format:
N
P_1 P_2 \ldots P_N

-----Output-----
Print \displaystyle \sum_{L=1}^{N-1} \sum_{R=L+1}^{N} X_{L,R}.

-----Sample Input-----
3
2 3 1

-----Sample Output-----
5

X_{1, 2} = 2, X_{1, 3} = 2, and X_{2, 3} = 1, so the sum is 2 + 2 + 1 = 5.
"""

def sum_of_second_largest_values(N: int, P: list) -> int:
    left_bigger = [0] + [i for i in range(N + 1)]
    right_bigger = [i + 1 for i in range(N + 1)] + [N + 1]
    E = [(v, i + 1) for (i, v) in enumerate(P)]
    E.sort()
    ans = 0
    for (v, i) in E:
        l0 = left_bigger[i]
        l1 = left_bigger[l0]
        r0 = right_bigger[i]
        r1 = right_bigger[r0]
        ans += ((r1 - r0) * (i - l0) + (r0 - i) * (l0 - l1)) * v
        left_bigger[r0] = l0
        right_bigger[l0] = r0
    return ans
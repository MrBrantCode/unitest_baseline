"""
QUESTION:
Contest T-shirts

Segtree has $ M $ contest T-shirts.

He decided to spend $ N $ days on the contest T-shirt alone, and told $ i = 1, 2, 3, \ dots, N $ "$ A_i $ T-shirt on the $ i $ day." I made a plan for $ N $ to wear.

However, if you keep the current plan, you may not be able to do the laundry in time, so I would like to change the plan if necessary so that I will not wear the same clothes for two consecutive days.

Find the minimum number of plans that need to be changed. It can be proved that the conditions can always be met by changing the plan under the given constraints.

input

Input is given from standard input in the following format.


$ M $ $ N $
$ A_1 $ $ A_2 $ $ \ ldots $ $ A_N $


output

Output the minimum number of plans that need to be changed.

However, insert a line break at the end.

Constraint

* $ 2 \ leq M \ leq 10 ^ 9 $
* $ 1 \ leq N \ leq 10 ^ 5 $
* $ 1 \ leq A_i \ leq M $
* All inputs are integers.



Input example 1


twenty three
2 2 1


Output example 1


1


Input example 2


3 6
1 1 1 2 2 3


Output example 2


2






Example

Input

2 3
2 2 1


Output

1
"""

def minimum_changes_for_tshirts(M, N, A):
    if M == 2:
        ans = N
        for i in range(2):
            t = 0
            for j in range(N):
                idx = (i + j) % 2 + 1
                if idx != A[j]:
                    t += 1
            ans = min(ans, t)
    else:
        ans = 0
        prev = A[0]
        for i in range(1, N):
            if prev == A[i]:
                ans += 1
                A[i] = -1
            prev = A[i]
    return ans
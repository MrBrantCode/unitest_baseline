"""
QUESTION:
There are N cards. The i-th card has an integer A_i written on it. For any two cards, the integers on those cards are different.

Using these cards, Takahashi and Aoki will play the following game:

* Aoki chooses an integer x.
* Starting from Takahashi, the two players alternately take a card. The card should be chosen in the following manner:
* Takahashi should take the card with the largest integer among the remaining card.
* Aoki should take the card with the integer closest to x among the remaining card. If there are multiple such cards, he should take the card with the smallest integer among those cards.
* The game ends when there is no card remaining.



You are given Q candidates for the value of x: X_1, X_2, ..., X_Q. For each i (1 \leq i \leq Q), find the sum of the integers written on the cards that Takahashi will take if Aoki chooses x = X_i.

Constraints

* 2 \leq N \leq 100 000
* 1 \leq Q \leq 100 000
* 1 \leq A_1 < A_2 < ... < A_N \leq 10^9
* 1 \leq X_i \leq 10^9 (1 \leq i \leq Q)
* All values in input are integers.

Input

Input is given from Standard Input in the following format:


N Q
A_1 A_2 ... A_N
X_1
X_2
:
X_Q


Output

Print Q lines. The i-th line (1 \leq i \leq Q) should contain the answer for x = X_i.

Examples

Input

5 5
3 5 7 11 13
1
4
9
10
13


Output

31
31
27
23
23


Input

4 3
10 20 30 40
2
34
34


Output

70
60
60
"""

import bisect
from itertools import accumulate

def calculate_takahashi_sums(N, Q, A, X):
    # Ensure the list A is sorted as per the problem constraints
    A.sort()
    
    # Initialize lists to store intermediate results
    accff = list(accumulate(A))
    fs = [A[i] if i % 2 == 0 else 0 for i in range(N)]
    accfs = list(accumulate(fs))
    
    xls = []
    xpt = []
    
    for i in range(N // 2):
        xls.append((A[2 * i + 1] + A[i + N // 2]) / 2)
        if i == 0:
            xpt.append(accff[N - 1] - accff[N // 2 - 1])
        else:
            xpt.append(accff[N - 1] - accff[i + N // 2 - 1] + accfs[2 * i - 1])
    
    results = []
    
    for x in X:
        idx = bisect.bisect_left(xls, x)
        if idx >= N // 2:
            results.append(xpt[-1])
        else:
            results.append(xpt[idx])
    
    return results
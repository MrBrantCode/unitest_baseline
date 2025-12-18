"""
QUESTION:
There is a stack of N cards, each of which has a non-negative integer written on it. The integer written on the i-th card from the top is A_i.

Snuke will repeat the following operation until two cards remain:

* Choose three consecutive cards from the stack.
* Eat the middle card of the three.
* For each of the other two cards, replace the integer written on it by the sum of that integer and the integer written on the card eaten.
* Return the two cards to the original position in the stack, without swapping them.



Find the minimum possible sum of the integers written on the last two cards remaining.

Constraints

* 2 \leq N \leq 18
* 0 \leq A_i \leq 10^9 (1\leq i\leq N)
* All values in input are integers.

Input

Input is given from Standard Input in the following format:


N
A_1 A_2 ... A_N


Output

Print the minimum possible sum of the integers written on the last two cards remaining.

Examples

Input

4
3 1 4 2


Output

16


Input

6
5 2 4 1 6 9


Output

51


Input

10
3 1 4 1 5 9 2 6 5 3


Output

115
"""

def minimum_sum_of_last_two_cards(N, A):
    memo = {}
    
    def kukan(l, r, el=1, er=1):
        em = el + er
        if l + 1 == r:
            return 0
        if l + 2 == r:
            return A[l + 1] * em
        t = (l, r, el, er)
        if t in memo:
            return memo[t]
        re = 10 ** 11
        for m in range(l + 1, r):
            tmp = kukan(l, m, el, em) + kukan(m, r, em, er) + A[m] * em
            if tmp < re:
                re = tmp
        memo[t] = re
        return re
    
    return A[0] + kukan(0, N - 1) + A[-1]
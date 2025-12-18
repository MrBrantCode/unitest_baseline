"""
QUESTION:
Takahashi is playing with N cards.

The i-th card has an integer X_i on it.

Takahashi is trying to create as many pairs of cards as possible satisfying one of the following conditions:

* The integers on the two cards are the same.
* The sum of the integers on the two cards is a multiple of M.



Find the maximum number of pairs that can be created.

Note that a card cannot be used in more than one pair.

Constraints

* 2≦N≦10^5
* 1≦M≦10^5
* 1≦X_i≦10^5

Input

The input is given from Standard Input in the following format:


N M
X_1 X_2 ... X_N


Output

Print the maximum number of pairs that can be created.

Examples

Input

7 5
3 1 4 1 5 9 2


Output

3


Input

15 10
1 5 6 10 11 11 11 20 21 25 25 26 99 99 99


Output

6
"""

import math

def max_pairs_from_cards(N, M, X):
    mod_arr = [{} for _ in range(M)]
    
    for x in X:
        d = mod_arr[x % M]
        if x in d:
            d[x] += 1
        else:
            d[x] = 1
    
    ans = 0
    
    if M == 1:
        return N // 2
    
    def calc_only_one(d):
        sum_v = sum(d.values())
        return sum_v // 2
    
    ans += calc_only_one(mod_arr[0])
    
    if M % 2 == 0:
        ans += calc_only_one(mod_arr[M // 2])
    
    def calc_two(d_S, d_T):
        res = 0
        if len(d_S) == 0:
            for v in d_T.values():
                res += v // 2
            return res
        elif len(d_T) == 0:
            for v in d_S.values():
                res += v // 2
            return res
        
        if sum(d_S.values()) < sum(d_T.values()):
            (d_S, d_T) = (d_T, d_S)
        
        cnt_S = sum(d_S.values())
        cnt_T = sum(d_T.values())
        remain_for_pair = cnt_S - cnt_T
        max_pair_cnt = sum([v // 2 for v in d_S.values()])
        pair_cnt = min(remain_for_pair // 2, max_pair_cnt)
        res = cnt_T + pair_cnt
        return res
    
    for i in range(1, math.ceil(M / 2)):
        ans += calc_two(mod_arr[i], mod_arr[M - i])
    
    return ans
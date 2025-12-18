"""
QUESTION:
Petya and Gena love playing table tennis. A single match is played according to the following rules: a match consists of multiple sets, each set consists of multiple serves. Each serve is won by one of the players, this player scores one point. As soon as one of the players scores t points, he wins the set; then the next set starts and scores of both players are being set to 0. As soon as one of the players wins the total of s sets, he wins the match and the match is over. Here s and t are some positive integer numbers.

To spice it up, Petya and Gena choose new numbers s and t before every match. Besides, for the sake of history they keep a record of each match: that is, for each serve they write down the winner. Serve winners are recorded in the chronological order. In a record the set is over as soon as one of the players scores t points and the match is over as soon as one of the players wins s sets.

Petya and Gena have found a record of an old match. Unfortunately, the sequence of serves in the record isn't divided into sets and numbers s and t for the given match are also lost. The players now wonder what values of s and t might be. Can you determine all the possible options?


-----Input-----

The first line contains a single integer n — the length of the sequence of games (1 ≤ n ≤ 10^5).

The second line contains n space-separated integers a_{i}. If a_{i} = 1, then the i-th serve was won by Petya, if a_{i} = 2, then the i-th serve was won by Gena.

It is not guaranteed that at least one option for numbers s and t corresponds to the given record.


-----Output-----

In the first line print a single number k — the number of options for numbers s and t.

In each of the following k lines print two integers s_{i} and t_{i} — the option for numbers s and t. Print the options in the order of increasing s_{i}, and for equal s_{i} — in the order of increasing t_{i}.


-----Examples-----
Input
5
1 2 1 2 1

Output
2
1 3
3 1

Input
4
1 1 1 1

Output
3
1 4
2 2
4 1

Input
4
1 2 1 2

Output
0

Input
8
2 1 2 1 1 1 1 1

Output
3
1 6
2 3
6 1
"""

import itertools

def find_possible_s_t(n, a):
    winner = a[-1]
    looser = 3 - winner
    serve_win_cnt = [0]
    serve_loose_cnt = [0]
    win_pos = [-1]
    loose_pos = [-1]
    result = []
    win_cnt = a.count(winner)
    
    for i in range(n):
        if a[i] == winner:
            win_pos.append(i)
        else:
            loose_pos.append(i)
        serve_win_cnt.append(serve_win_cnt[-1] + (a[i] == winner))
        serve_loose_cnt.append(serve_loose_cnt[-1] + (a[i] == looser))
    
    win_pos += [n * 10] * n
    loose_pos += [n * 10] * n
    serve_win_cnt += [0] * n
    serve_loose_cnt += [0] * n
    
    for t in itertools.chain(list(range(1, 1 + win_cnt // 2)), [win_cnt]):
        s = l = i = 0
        sw = sl = 0
        while i < n:
            xw = win_pos[serve_win_cnt[i] + t]
            xl = loose_pos[serve_loose_cnt[i] + t]
            if xw < xl:
                s += 1
            else:
                l += 1
            i = min(xw, xl) + 1
        if s > l and i <= n and (serve_win_cnt[i] == win_cnt):
            result.append((s, t))
    
    k = len(result)
    options = sorted(result)
    
    return k, options
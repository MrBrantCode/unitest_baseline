"""
QUESTION:
Robbers, who attacked the Gerda's cab, are very successful in covering from the kingdom police. To make the goal of catching them even harder, they use their own watches.

First, as they know that kingdom police is bad at math, robbers use the positional numeral system with base 7. Second, they divide one day in n hours, and each hour in m minutes. Personal watches of each robber are divided in two parts: first of them has the smallest possible number of places that is necessary to display any integer from 0 to n - 1, while the second has the smallest possible number of places that is necessary to display any integer from 0 to m - 1. Finally, if some value of hours or minutes can be displayed using less number of places in base 7 than this watches have, the required number of zeroes is added at the beginning of notation.

Note that to display number 0 section of the watches is required to have at least one place.

Little robber wants to know the number of moments of time (particular values of hours and minutes), such that all digits displayed on the watches are distinct. Help her calculate this number.


-----Input-----

The first line of the input contains two integers, given in the decimal notation, n and m (1 ≤ n, m ≤ 10^9) — the number of hours in one day and the number of minutes in one hour, respectively.


-----Output-----

Print one integer in decimal notation — the number of different pairs of hour and minute, such that all digits displayed on the watches are distinct.


-----Examples-----
Input
2 3

Output
4

Input
8 2

Output
5



-----Note-----

In the first sample, possible pairs are: (0: 1), (0: 2), (1: 0), (1: 2).

In the second sample, possible pairs are: (02: 1), (03: 1), (04: 1), (05: 1), (06: 1).
"""

from itertools import permutations

def str_base(number, base):
    if number < 0:
        return '-' + str_base(-number, base)
    (d, m) = divmod(number, base)
    if d > 0:
        return str_base(d, base) + str(m)
    return str(m)

def count_distinct_time_pairs(n, m):
    max_h = str_base(n - 1, 7)
    max_m = str_base(m - 1, 7)
    len_h = len(max_h)
    len_m = len(max_m)
    result = 0
    
    for p in permutations(list(range(7)), len_h + len_m):
        if str(''.join(map(str, p[:len_h]))) <= max_h and str(''.join(map(str, p[len_h:]))) <= max_m:
            result += 1
    
    return result
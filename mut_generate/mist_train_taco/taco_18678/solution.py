"""
QUESTION:
The year of 2012 is coming...

According to an ancient choradrican legend in this very year, in 2012, Diablo and his brothers Mephisto and Baal will escape from hell, and innumerable hordes of demons will enslave the human world. But seven brave heroes have already gathered on the top of a mountain Arreat to protect us mere mortals from the effect of this terrible evil.

The seven great heroes are: amazon Anka, barbarian Chapay, sorceress Cleo, druid Troll, necromancer Dracul, paladin Snowy and a professional hit girl Hexadecimal. Heroes already know how much experience will be given for each of the three megabosses: a for Mephisto, b for Diablo and c for Baal.

Here's the problem: heroes are as much as seven and megabosses are only three! Then our heroes decided to split into three teams, where each team will go to destroy their own megaboss. Each team member will receive a <image> of experience, rounded down, where x will be the amount of experience for the killed megaboss and y — the number of people in the team.

Heroes do not want to hurt each other's feelings, so they want to split into teams so that the difference between the hero who received the maximum number of experience and the hero who received the minimum number of experience were minimal. Since there can be several divisions into teams, then you need to find the one in which the total amount of liking in teams were maximum.

It is known that some heroes like others. But if hero p likes hero q, this does not mean that the hero q likes hero p. No hero likes himself.

The total amount of liking in teams is the amount of ordered pairs (p, q), such that heroes p and q are in the same group, and hero p likes hero q (but it is not important if hero q likes hero p). In case of heroes p and q likes each other and they are in the same group, this pair should be counted twice, as (p, q) and (q, p).

A team can consist even of a single hero, but it is important that every megaboss was destroyed. All heroes must be involved in the campaign against evil. None of the heroes can be in more than one team.

It is guaranteed that every hero is able to destroy any megaboss alone.

Input

The first line contains a single non-negative integer n (0 ≤ n ≤ 42) — amount of liking between the heroes. Next n lines describe liking in the form "p likes q", meaning that the hero p likes the hero q (p ≠  q). Every liking is described in the input exactly once, no hero likes himself.

In the last line are given three integers a, b and c (1 ≤ a, b, c ≤ 2·109), separated by spaces: the experience for Mephisto, the experience for Diablo and experience for Baal.

In all the pretests, except for examples from the statement, the following condition is satisfied: a = b = c.

Output

Print two integers — the minimal difference in the experience between two heroes who will receive the maximum and minimum number of experience points, and the maximal total amount of liking in teams (the number of friendships between heroes that end up in one team).

When calculating the second answer, the team division should satisfy the difference-minimizing contraint. I.e. primary you should minimize the difference in the experience and secondary you should maximize the total amount of liking.

Examples

Input

3
Troll likes Dracul
Dracul likes Anka
Snowy likes Hexadecimal
210 200 180


Output

30 3


Input

2
Anka likes Chapay
Chapay likes Anka
10000 50 50


Output

1950 2

Note

A note to first example: it the first team should be Dracul, Troll and Anka, in the second one Hexadecimal and Snowy, and in the third Cleo и Chapay.
"""

from itertools import combinations, product

def minimize_experience_difference_and_maximize_liking(n, likings, experience):
    Teams = [[1, 1, 5], [1, 2, 4], [1, 3, 3], [2, 2, 3]]
    Names = {
        'Anka': 0,
        'Chapay': 1,
        'Cleo': 2,
        'Dracul': 3,
        'Hexadecimal': 4,
        'Snowy': 5,
        'Troll': 6
    }
    graph = [[0] * 7 for _ in range(7)]
    
    for (p, q) in likings:
        p = Names[p]
        q = Names[q]
        graph[p][q] = 1
    
    a, b, c = sorted(experience)
    E_diff_star = float('inf')
    team_all = []
    
    for (t1, t2, t3) in Teams:
        E = [a // t1, b // t2, c // t3]
        E_diff = max(E) - min(E)
        if E_diff < E_diff_star:
            E_diff_star = E_diff
            team_all = [[t1, t2, t3]]
        elif E_diff == E_diff_star:
            team_all.append([t1, t2, t3])
    
    liking = 0
    for team in team_all:
        for te2 in combinations(set(range(7)), team[2]):
            te2 = set(te2)
            left = set(range(7)) - te2
            L2 = sum((graph[p][q] for (p, q) in product(te2, te2)))
            for te1 in combinations(left, team[1]):
                te1 = set(te1)
                te0 = left - te1
                L1 = sum((graph[p][q] for (p, q) in product(te1, te1)))
                L0 = sum((graph[p][q] for (p, q) in product(te0, te0)))
                L = L2 + L1 + L0
                if L > liking:
                    liking = L
    
    return E_diff_star, liking
"""
QUESTION:
One very important person has a piece of paper in the form of a rectangle a × b.

Also, he has n seals. Each seal leaves an impression on the paper in the form of a rectangle of the size x_{i} × y_{i}. Each impression must be parallel to the sides of the piece of paper (but seal can be rotated by 90 degrees).

A very important person wants to choose two different seals and put them two impressions. Each of the selected seals puts exactly one impression. Impressions should not overlap (but they can touch sides), and the total area occupied by them should be the largest possible. What is the largest area that can be occupied by two seals?


-----Input-----

The first line contains three integer numbers n, a and b (1 ≤ n, a, b ≤ 100).

Each of the next n lines contain two numbers x_{i}, y_{i} (1 ≤ x_{i}, y_{i} ≤ 100).


-----Output-----

Print the largest total area that can be occupied by two seals. If you can not select two seals, print 0.


-----Examples-----
Input
2 2 2
1 2
2 1

Output
4

Input
4 10 9
2 3
1 1
5 10
9 11

Output
56

Input
3 10 10
6 6
7 7
20 5

Output
0



-----Note-----

In the first example you can rotate the second seal by 90 degrees. Then put impression of it right under the impression of the first seal. This will occupy all the piece of paper.

In the second example you can't choose the last seal because it doesn't fit. By choosing the first and the third seals you occupy the largest area.

In the third example there is no such pair of seals that they both can fit on a piece of paper.
"""

def largest_area_of_two_seals(n, a, b, seals):
    MINUS_INF = -10 ** 9

    def fit(w, h, s1, s2):
        return subfit(w, h, s1, s2) or subfit(w, h, rev(s1), s2) or subfit(w, h, s1, rev(s2)) or subfit(h, w, s1, s2)

    def subfit(w, h, s1, s2):
        return (s1[0] + s2[0] <= w and s1[1] <= h and s2[1] <= h) or (s1[1] + s2[1] <= h and s1[0] <= w and s2[0] <= w)

    def rev(s):
        return (s[1], s[0])

    res = MINUS_INF
    for i, s1 in enumerate(seals):
        for s2 in seals[i + 1:]:
            if fit(a, b, s1, s2):
                res = max(res, s1[0] * s1[1] + s2[0] * s2[1])
    res = max(res, 0)
    return res
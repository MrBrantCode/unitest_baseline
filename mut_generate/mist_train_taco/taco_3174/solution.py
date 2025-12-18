"""
QUESTION:
The football season has just ended in Berland. According to the rules of Berland football, each match is played between two teams. The result of each match is either a draw, or a victory of one of the playing teams. If a team wins the match, it gets w points, and the opposing team gets 0 points. If the game results in a draw, both teams get d points.

The manager of the Berland capital team wants to summarize the results of the season, but, unfortunately, all information about the results of each match is lost. The manager only knows that the team has played n games and got p points for them.

You have to determine three integers x, y and z — the number of wins, draws and loses of the team. If there are multiple answers, print any of them. If there is no suitable triple (x, y, z), report about it.

Input

The first line contains four integers n, p, w and d (1 ≤ n ≤ 10^{12}, 0 ≤ p ≤ 10^{17}, 1 ≤ d < w ≤ 10^{5}) — the number of games, the number of points the team got, the number of points awarded for winning a match, and the number of points awarded for a draw, respectively. Note that w > d, so the number of points awarded for winning is strictly greater than the number of points awarded for draw.

Output

If there is no answer, print -1.

Otherwise print three non-negative integers x, y and z — the number of wins, draws and losses of the team. If there are multiple possible triples (x, y, z), print any of them. The numbers should meet the following conditions: 

  * x ⋅ w + y ⋅ d = p, 
  * x + y + z = n. 

Examples

Input


30 60 3 1


Output


17 9 4


Input


10 51 5 4


Output


-1


Input


20 0 15 5


Output


0 0 20

Note

One of the possible answers in the first example — 17 wins, 9 draws and 4 losses. Then the team got 17 ⋅ 3 + 9 ⋅ 1 = 60 points in 17 + 9 + 4 = 30 games.

In the second example the maximum possible score is 10 ⋅ 5 = 50. Since p = 51, there is no answer.

In the third example the team got 0 points, so all 20 games were lost.
"""

def calculate_football_results(n, p, w, d):
    def extendedEuclideanAlgorithm(old_r, r):
        negative = False
        (s, old_t) = (0, 0)
        (old_s, t) = (1, 1)
        if r < 0:
            r = abs(r)
            negative = True
        while r > 0:
            q = old_r // r
            (r, old_r) = (old_r - q * r, r)
            (s, old_s) = (old_s - q * s, s)
            (t, old_t) = (old_t - q * t, t)
        if negative:
            old_t = old_t * -1
        return (old_r, old_s, old_t)

    (mcd, s, t) = extendedEuclideanAlgorithm(w, d)
    if p % mcd == 0:
        (a1, b1, c1) = (-w // mcd, d // mcd, p // mcd)
        (x1, y1) = (s * c1, t * c1)
        k = y1 * mcd // w
        x0 = x1 + d * k // mcd
        y0 = y1 - w * k // mcd
        if x0 + y0 <= n and x0 >= 0 and (y0 >= 0):
            return (x0, y0, n - x0 - y0)
        else:
            return (-1, -1, -1)
    else:
        return (-1, -1, -1)
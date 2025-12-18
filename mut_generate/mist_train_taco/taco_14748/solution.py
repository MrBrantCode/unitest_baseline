"""
QUESTION:
## A Knight's Tour

A knight's tour is a sequence of moves of a knight on a chessboard such that the knight visits every square only once.

https://en.wikipedia.org/wiki/Knight%27s_tour

Traditional chess boards are 8x8 grids, but for this kata we are interested in generating tours for any square board sizes.

You will be asked to find a knight's path for any NxN board from any start position.

I have provided a tool to visualize the output of your code at the following link: http://jsfiddle.net/7sbyya59/2/

EDIT: The expected output is a 2D array `(n x 2)` comprised of the `[x,y]` coordinates of the Knight's path taken in sequential order. (e.g. `[[2,3],[4,4],...,[x,y]]`)

All test cases will have a passing solution.

-dg
"""

def knights_tour(start, size):
    MOVES = [(-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2)]

    def genNeighs(pos):
        return ((pos[0] + dx, pos[1] + dy) for (dx, dy) in MOVES if (pos[0] + dx, pos[1] + dy) in Warnsdorf_DP)

    def travel(pos):
        neighs = sorted(((Warnsdorf_DP[n], n) for n in genNeighs(pos)))
        for (nSubNeighs, neigh) in neighs:
            del Warnsdorf_DP[neigh]
            path.append(neigh)
            subNeighs = list(genNeighs(neigh))
            for n in subNeighs:
                Warnsdorf_DP[n] -= 1
            travel(neigh)
            if not Warnsdorf_DP:
                break
            else:
                for n in subNeighs:
                    Warnsdorf_DP[n] += 1
                Warnsdorf_DP[path.pop()] = nSubNeighs

    (path, Warnsdorf_DP) = ([start], {(x, y): 0 for x in range(size) for y in range(size) if (x, y) != start})
    for pos in Warnsdorf_DP:
        Warnsdorf_DP[pos] = sum((1 for _ in genNeighs(pos)))
    travel(start)
    return path
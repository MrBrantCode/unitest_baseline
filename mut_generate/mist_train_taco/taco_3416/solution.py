"""
QUESTION:
Peace, which was supposed to last forever, suddenly ended. The Demon King, who had been sealed long ago, has finally revived. But when the world was about to be covered in darkness, a brave man appeared. The hero then set out on a journey to collect legendary crystals scattered around the world. Legend has it that if you can collect all the crystals, you can summon the legendary dragon god who can fulfill any wish. With the help of the dragon god, it should be possible to defeat the Demon King.

Crystals are scattered all over the world. The hero needs to collect them one by one by his own hands. This is because if someone other than the hero gets the crystal, it may be stolen by the Demon King's minions. A hero can travel only one Euclidean distance per day.

But there is one serious problem here. The Demon King constantly disperses the darkness of the miasma, and the place contaminated with the miasma turns into a land of death that no one can enter. Even a brave man cannot enter the place. Furthermore, since the miasma spreads concentrically with time, the area where the hero can move decreases with the passage of time. Miasma has been confirmed to spread by an Euclidean distance of 1 per day. And the hero cannot take the crystal on the boundary line. We also know that the newly resurrected Demon King will not move to store power.

The hero must get the crystal as soon as possible. But if it's not possible to get all the crystals, you'll have to think of another way. Therefore, I would like you to create a program to find out if you can get all the crystals from the initial position of the hero, the place where the demon king was resurrected, and the position where the crystals exist.

By the way, the brave does not get tired. And I don't sleep. Keep moving and collect crystals until you collect all the crystals and save the world! !!



Input

The input consists of multiple test cases. The first line of each test case gives the five integers n (0 <n <= 20), hx, hy, dx, and dy. n is the number of crystals, (hx, hy) is the position of the hero at the moment the Demon King was resurrected, and (dx, dy) is the position where the Demon King was resurrected. The n lines that follow are given the two integers cx, cy, that represent the position of each crystal. Input ends when n = hx = hy = dx = dy = 0, which is not included in the test case.

All coordinates given in the input are guaranteed to be integers with an absolute value of 1000 or less.

Output

For each test case, output "YES" if you can collect all the crystals, and "NO" if not.

Example

Input

2 0 0 10 10
1 1
4 4
2 0 0 10 10
1 1
6 6
2 0 0 10 10
1 1
5 5
0 0 0 0 0


Output

YES
NO
NO
"""

from math import sqrt

def can_collect_all_crystals(n, hx, hy, dx, dy, crystals):
    def dfs(point, remain, elapsed):
        if not remain:
            return True
        next_c = set()
        for c in remain:
            new_elapsed = elapsed + adj[point][c]
            if new_elapsed >= from_d[c]:
                return False
            next_c.add((c, new_elapsed))
        for (c, new_elapsed) in next_c:
            remain.remove(c)
            if dfs(c, remain, new_elapsed):
                return True
            remain.add(c)
        return False

    from_d = tuple((sqrt((cx - dx) ** 2 + (cy - dy) ** 2) for (cx, cy) in crystals))
    crystals.append((hx, hy))
    adj = tuple((tuple((sqrt((px - qx) ** 2 + (py - qy) ** 2) for (qx, qy) in crystals)) for (px, py) in crystals))
    
    return dfs(n, set(range(n)), 0)
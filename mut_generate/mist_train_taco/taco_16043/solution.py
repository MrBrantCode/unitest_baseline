"""
QUESTION:
Recently a new building with a new layout was constructed in Monocarp's hometown. According to this new layout, the building consists of three types of apartments: three-room, five-room, and seven-room apartments. It's also known that each room of each apartment has exactly one window. In other words, a three-room apartment has three windows, a five-room — five windows, and a seven-room — seven windows.

Monocarp went around the building and counted $n$ windows. Now he is wondering, how many apartments of each type the building may have.

Unfortunately, Monocarp only recently has learned to count, so he is asking you to help him to calculate the possible quantities of three-room, five-room, and seven-room apartments in the building that has $n$ windows. If there are multiple answers, you can print any of them.

Here are some examples:

  if Monocarp has counted $30$ windows, there could have been $2$ three-room apartments, $2$ five-room apartments and $2$ seven-room apartments, since $2 \cdot 3 + 2 \cdot 5 + 2 \cdot 7 = 30$;  if Monocarp has counted $67$ windows, there could have been $7$ three-room apartments, $5$ five-room apartments and $3$ seven-room apartments, since $7 \cdot 3 + 5 \cdot 5 + 3 \cdot 7 = 67$;  if Monocarp has counted $4$ windows, he should have mistaken since no building with the aforementioned layout can have $4$ windows. 


-----Input-----

Th first line contains one integer $t$ ($1 \le t \le 1000$) — the number of test cases.

The only line of each test case contains one integer $n$ ($1 \le n \le 1000$) — the number of windows in the building.


-----Output-----

For each test case, if a building with the new layout and the given number of windows just can't exist, print $-1$.

Otherwise, print three non-negative integers — the possible number of three-room, five-room, and seven-room apartments. If there are multiple answers, print any of them.


-----Example-----
Input
4
30
67
4
14

Output
2 2 2
7 5 3
-1
0 0 2
"""

def find_apartment_distribution(n):
    if n in [1, 2, 4]:
        return -1
    elif n == 3:
        return (1, 0, 0)
    else:
        k = n // 5 - 1
        n = n - 5 * k
        if n == 5:
            return (0, k + 1, 0)
        elif n == 6:
            return (2, k, 0)
        elif n == 7:
            return (0, k, 1)
        elif n == 8:
            return (1, k + 1, 0)
        elif n == 9:
            return (3, k, 0)
        else:
            return -1
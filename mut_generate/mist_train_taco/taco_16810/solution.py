"""
QUESTION:
You are given two non-negative integers L and R.
We will choose two integers i and j such that L \leq i < j \leq R.
Find the minimum possible value of (i \times j) \mbox{ mod } 2019.

-----Constraints-----
 - All values in input are integers.
 - 0 \leq L < R \leq 2 \times 10^9

-----Input-----
Input is given from Standard Input in the following format:
L R

-----Output-----
Print the minimum possible value of (i \times j) \mbox{ mod } 2019 when i and j are chosen under the given condition.

-----Sample Input-----
2020 2040

-----Sample Output-----
2

When (i, j) = (2020, 2021), (i \times j) \mbox{ mod } 2019  = 2.
"""

def find_min_mod_2019(L, R):
    diff = R - L
    if diff >= 2018:
        return 0
    else:
        min_ = 2 ** 20
        p = L // 2019
        q = L % 2019
        for xi in range(L, R):
            qi = (q + (xi - L)) % 2019
            if qi == 0:
                return 0
            for xj in range(xi + 1, R + 1):
                qj = (q + (xj - L)) % 2019
                if qj == 0:
                    return 0
                else:
                    qij = qi * qj % 2019
                    if qij < min_:
                        min_ = qij
        return min_
"""
QUESTION:
Ivar the Boneless is a great leader. He is trying to capture Kattegat from Lagertha. The war has begun and wave after wave Ivar's warriors are falling in battle.

Ivar has $n$ warriors, he places them on a straight line in front of the main gate, in a way that the $i$-th warrior stands right after $(i-1)$-th warrior. The first warrior leads the attack.

Each attacker can take up to $a_i$ arrows before he falls to the ground, where $a_i$ is the $i$-th warrior's strength.

Lagertha orders her warriors to shoot $k_i$ arrows during the $i$-th minute, the arrows one by one hit the first still standing warrior. After all Ivar's warriors fall and all the currently flying arrows fly by, Thor smashes his hammer and all Ivar's warriors get their previous strengths back and stand up to fight again. In other words, if all warriors die in minute $t$, they will all be standing to fight at the end of minute $t$.

The battle will last for $q$ minutes, after each minute you should tell Ivar what is the number of his standing warriors.


-----Input-----

The first line contains two integers $n$ and $q$ ($1 \le n, q \leq 200\,000$) — the number of warriors and the number of minutes in the battle.

The second line contains $n$ integers $a_1, a_2, \ldots, a_n$ ($1 \leq a_i \leq 10^9$) that represent the warriors' strengths.

The third line contains $q$ integers $k_1, k_2, \ldots, k_q$ ($1 \leq k_i \leq 10^{14}$), the $i$-th of them represents Lagertha's order at the $i$-th minute: $k_i$ arrows will attack the warriors.


-----Output-----

Output $q$ lines, the $i$-th of them is the number of standing warriors after the $i$-th minute.


-----Examples-----
Input
5 5
1 2 1 2 1
3 10 1 1 1

Output
3
5
4
4
3

Input
4 4
1 2 3 4
9 1 10 6

Output
1
4
4
1



-----Note-----

In the first example:   after the 1-st minute, the 1-st and 2-nd warriors die.  after the 2-nd minute all warriors die (and all arrows left over are wasted), then they will be revived thus answer is 5 — all warriors are alive.  after the 3-rd minute, the 1-st warrior dies.  after the 4-th minute, the 2-nd warrior takes a hit and his strength decreases by 1.  after the 5-th minute, the 2-nd warrior dies.
"""

from itertools import accumulate

def calculate_standing_warriors(n, q, warriors_strength, arrows_per_minute):
    def arr_sum(arr):
        arr.insert(0, 0)
        return list(accumulate(arr, lambda x, y: x + y))

    def bs(be, en, x, arr):
        ix = be
        while be < en:
            mid = (be + en) // 2
            val = arr[mid] - arr[ix]
            if val == x:
                return mid
            elif val > x:
                en = mid
            else:
                be = mid + 1
        return en

    cum = arr_sum(warriors_strength)
    ix = 0
    ext = 0
    result = []

    for i in range(q):
        if ext > arrows_per_minute[i]:
            result.append(n - ix + 1)
            ext -= arrows_per_minute[i]
        elif ext == arrows_per_minute[i]:
            ext = 0
            if ix >= n:
                ix = 0
            result.append(n - ix)
        else:
            arrows_per_minute[i] -= ext
            ext = 0
            nx = bs(ix, n, arrows_per_minute[i], cum)
            if cum[nx] - cum[ix] <= arrows_per_minute[i]:
                if nx >= n:
                    ix = 0
                    nx = 0
                result.append(n - nx)
            else:
                ext = cum[nx] - cum[ix] - arrows_per_minute[i]
                result.append(n - nx + 1)
            ix = nx

    return result
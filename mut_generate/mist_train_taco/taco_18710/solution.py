"""
QUESTION:
To destroy humanity, The Monster Association sent $n$ monsters to Earth's surface. The $i$-th monster has health $h_i$ and power $p_i$.

With his last resort attack, True Spiral Incineration Cannon, Genos can deal $k$ damage to all monsters alive. In other words, Genos can reduce the health of all monsters by $k$ (if $k > 0$) with a single attack.

However, after every attack Genos makes, the monsters advance. With their combined efforts, they reduce Genos' attack damage by the power of the $^\dagger$weakest monster $^\ddagger$alive. In other words, the minimum $p_i$ among all currently living monsters is subtracted from the value of $k$ after each attack.

$^\dagger$The Weakest monster is the one with the least power.

$^\ddagger$A monster is alive if its health is strictly greater than $0$.

Will Genos be successful in killing all the monsters?


-----Input-----

The first line of the input contains a single integer $t$ ($1 \le t \le 100$) — the number of test cases. The description of test cases follows.

The first line of each test case contains two integers, $n$ and $k$ ($1 \le n, k \le 10^5$) — the number of monsters and Genos' initial attack damage. Then two lines follow, each containing $n$ integers describing the arrays $h$ and $p$ ($1 \le h_i, p_i \le 10^9$).

It's guaranteed that the sum of $n$ over all test cases does not exceed $2 \cdot 10^5$.


-----Output-----

For each test case, print the answer — "YES" (without quotes) if Genos could kill all monsters and "NO" otherwise.


-----Examples-----

Input
3
6 7
18 5 13 9 10 1
2 7 2 1 2 6
3 4
5 5 5
4 4 4
3 2
2 1 3
1 1 1
Output
YES
NO
YES


-----Note-----

In the first example, after Genos' first attack, $h$ and $k$ will update to:

$h: [11,0,6,2,3,0]$

$k: 7-1 = 6$

After second attack:

$h: [5,0,0,0,0,0]$

$k: 6-2 = 4$

After third attack:

$h: [1,0,0,0,0,0]$

$k: 4-2 = 2$

After fourth attack:

$h: [0,0,0,0,0,0]$

As Genos could kill all monsters, the answer is YES.
"""

def can_genos_kill_all_monsters(n, k, h, p):
    """
    Determines if Genos can kill all monsters given their health and power values.

    Parameters:
    n (int): Number of monsters.
    k (int): Initial attack damage.
    h (list): List of health values of the monsters.
    p (list): List of power values of the monsters.

    Returns:
    str: "YES" if Genos can kill all monsters, "NO" otherwise.
    """
    arr = sorted([[p[i], h[i]] for i in range(n)])
    offset = 0
    for i in range(n):
        (p_i, h_i) = arr[i]
        h_i -= offset
        if h_i <= 0:
            continue
        k -= p_i if i > 0 else 0
        if k >= h_i:
            offset += k
            continue
        elif k <= 0:
            return 'NO'
        D = (p_i + 2 * k) ** 2 - 8 * p_i * h_i
        if D < 0:
            return 'NO'
        x1 = math.ceil((p_i + 2 * k - D ** 0.5) / (2 * p_i))
        if x1 > 0 and p_i * x1 ** 2 - x1 * (p_i + 2 * k) + 2 * h_i <= 0:
            offset += k * x1 - p_i * (x1 - 1) * x1 // 2
            k -= p_i * (x1 - 1)
        else:
            return 'NO'
    return 'YES'
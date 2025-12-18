"""
QUESTION:
There is a building with n rooms, numbered 1 to n.
We can move from any room to any other room in the building.
Let us call the following event a move: a person in some room i goes to another room j~ (i \neq j).
Initially, there was one person in each room in the building.
After that, we know that there were exactly k moves happened up to now.
We are interested in the number of people in each of the n rooms now. How many combinations of numbers of people in the n rooms are possible?
Find the count modulo (10^9 + 7).

-----Constraints-----
 - All values in input are integers.
 - 3 \leq n \leq 2 \times 10^5
 - 2 \leq k \leq 10^9

-----Input-----
Input is given from Standard Input in the following format:
n k

-----Output-----
Print the number of possible combinations of numbers of people in the n rooms now, modulo (10^9 + 7).

-----Sample Input-----
3 2

-----Sample Output-----
10

Let c_1, c_2, and c_3 be the number of people in Room 1, 2, and 3 now, respectively. There are 10 possible combination of (c_1, c_2, c_3):
 - (0, 0, 3)
 - (0, 1, 2)
 - (0, 2, 1)
 - (0, 3, 0)
 - (1, 0, 2)
 - (1, 1, 1)
 - (1, 2, 0)
 - (2, 0, 1)
 - (2, 1, 0)
 - (3, 0, 0)
For example, (c_1, c_2, c_3) will be (0, 1, 2) if the person in Room 1 goes to Room 2 and then one of the persons in Room 2 goes to Room 3.
"""

def count_possible_combinations(n: int, k: int, mod: int = 10**9 + 7) -> int:
    def cmb(n, r, mod):
        if r < 0 or r > n:
            return 0
        r = min(r, n - r)
        return g1[n] * g2[r] * g2[n - r] % mod

    n = n * 2
    r = min(n, k + 1)
    g1 = [1, 1]
    g2 = [1, 1]
    inverse = [0, 1]

    for i in range(2, n + 1):
        g1.append(g1[-1] * i % mod)
        inverse.append(-inverse[mod % i] * (mod // i) % mod)
        g2.append(g2[-1] * inverse[-1] % mod)

    ans = 0
    for i in range(r):
        ans += cmb(n // 2, i, mod) * cmb(n // 2 - 1, i, mod)

    if k == 1:
        ans -= 1

    return ans % mod
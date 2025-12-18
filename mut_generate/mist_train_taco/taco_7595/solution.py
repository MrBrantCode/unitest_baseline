"""
QUESTION:
Taro has decided to move. Taro has a lot of luggage, so I decided to ask a moving company to carry the luggage. Since there are various weights of luggage, I asked them to arrange them in order from the lightest one for easy understanding, but the mover left the luggage in a different order. So Taro tried to sort the luggage, but the luggage is heavy and requires physical strength to carry. Each piece of luggage can be carried from where it is now to any place you like, such as between other pieces of luggage or at the edge of the piece of luggage, but carrying one piece of luggage uses as much physical strength as the weight of that piece of luggage. Taro doesn't have much physical strength, so I decided to think of a way to arrange the luggage in order from the lightest one without using as much physical strength as possible.

Constraints

> 1 ≤ n ≤ 105
> 1 ≤ xi ≤ n (1 ≤ i ≤ n)
> xi ≠ xj (1 ≤ i, j ≤ n and i ≠ j)
>

* All inputs are given as integers

Input

> n
> x1 x2 ... xn
>

* n represents the number of luggage that Taro has
* x1 to xn represent the weight of each piece of luggage, and are currently arranged in the order of x1, x2, ..., xn.

Output

> S
>

* Output the total S of the minimum physical strength required to arrange the luggage in order from the lightest, but output the line break at the end

Examples

Input

4
1 4 2 3


Output

4


Input

5
1 5 3 2 4


Output

7


Input

7
1 2 3 4 5 6 7


Output

0


Input

8
6 2 1 3 8 5 4 7


Output

19
"""

import math

class FenwickTree:
    def __init__(self, a_list, f, default):
        self.N = len(a_list)
        self.bit = a_list[:]
        self.f = f
        self.default = default
        for _ in range(self.N, 1 << math.ceil(math.log(self.N, 2))):
            self.bit.append(self.default)
        for i in range(self.N - 1):
            self.bit[i | i + 1] = self.f(self.bit[i | i + 1], self.bit[i])

    def update(self, i, val):
        while i < self.N:
            self.bit[i] = self.f(self.bit[i], val)
            i |= i + 1

    def query(self, n):
        ret = 0
        while n >= 0:
            ret = self.f(ret, self.bit[n])
            n = (n & n + 1) - 1
        return ret

def calculate_minimum_physical_strength(n, weights):
    dp = FenwickTree([0] * n, lambda x, y: max(x, y), 0)
    for (x, i) in sorted(((x, i) for (i, x) in enumerate(weights))):
        dp.update(i, dp.query(i) + x)
    return n * (n + 1) // 2 - dp.query(n - 1)
"""
QUESTION:
On vacations n pupils decided to go on excursion and gather all together. They need to overcome the path with the length l meters. Each of the pupils will go with the speed equal to v1. To get to the excursion quickly, it was decided to rent a bus, which has seats for k people (it means that it can't fit more than k people at the same time) and the speed equal to v2. In order to avoid seasick, each of the pupils want to get into the bus no more than once.

Determine the minimum time required for all n pupils to reach the place of excursion. Consider that the embarkation and disembarkation of passengers, as well as the reversal of the bus, take place immediately and this time can be neglected. 

Input

The first line of the input contains five positive integers n, l, v1, v2 and k (1 ≤ n ≤ 10 000, 1 ≤ l ≤ 109, 1 ≤ v1 < v2 ≤ 109, 1 ≤ k ≤ n) — the number of pupils, the distance from meeting to the place of excursion, the speed of each pupil, the speed of bus and the number of seats in the bus. 

Output

Print the real number — the minimum time in which all pupils can reach the place of excursion. Your answer will be considered correct if its absolute or relative error won't exceed 10 - 6.

Examples

Input

5 10 1 2 5


Output

5.0000000000


Input

3 6 1 2 1


Output

4.7142857143

Note

In the first sample we should immediately put all five pupils to the bus. The speed of the bus equals 2 and the distance is equal to 10, so the pupils will reach the place of excursion in time 10 / 2 = 5.
"""

def calculate_minimum_time(n, l, v1, v2, k):
    n = (n + k - 1) // k
    t0 = l / v1
    t1 = l / v2
    
    if n == 1:
        return t1
    else:
        for _ in range(50):
            t = (t0 + t1) / 2
            d2 = v2 * t
            x2 = (d2 - l) / (n - 1) / 2
            u2 = (d2 - (n - 1) * x2) / n
            tt = u2 / v2 + (l - u2) / v1
            if tt > t:
                t1 = t
            else:
                t0 = t
        return t
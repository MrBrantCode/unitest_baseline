"""
QUESTION:
On vacations n pupils decided to go on excursion and gather all together. They need to overcome the path with the length l meters. Each of the pupils will go with the speed equal to v_1. To get to the excursion quickly, it was decided to rent a bus, which has seats for k people (it means that it can't fit more than k people at the same time) and the speed equal to v_2. In order to avoid seasick, each of the pupils want to get into the bus no more than once.

Determine the minimum time required for all n pupils to reach the place of excursion. Consider that the embarkation and disembarkation of passengers, as well as the reversal of the bus, take place immediately and this time can be neglected. 


-----Input-----

The first line of the input contains five positive integers n, l, v_1, v_2 and k (1 ≤ n ≤ 10 000, 1 ≤ l ≤ 10^9, 1 ≤ v_1 < v_2 ≤ 10^9, 1 ≤ k ≤ n) — the number of pupils, the distance from meeting to the place of excursion, the speed of each pupil, the speed of bus and the number of seats in the bus. 


-----Output-----

Print the real number — the minimum time in which all pupils can reach the place of excursion. Your answer will be considered correct if its absolute or relative error won't exceed 10^{ - 6}.


-----Examples-----
Input
5 10 1 2 5

Output
5.0000000000

Input
3 6 1 2 1

Output
4.7142857143



-----Note-----

In the first sample we should immediately put all five pupils to the bus. The speed of the bus equals 2 and the distance is equal to 10, so the pupils will reach the place of excursion in time 10 / 2 = 5.
"""

def calculate_minimum_time(n: int, l: int, v1: int, v2: int, k: int) -> float:
    """
    Calculate the minimum time required for all n pupils to reach the place of excursion.

    Parameters:
    n (int): The number of pupils.
    l (int): The distance from the meeting point to the place of excursion.
    v1 (int): The speed of each pupil.
    v2 (int): The speed of the bus.
    k (int): The number of seats in the bus.

    Returns:
    float: The minimum time in which all pupils can reach the place of excursion.
    """
    m = (n - 1) // k + 1
    v = v1 + v2
    x = l * v * v2 / (m * v * v2 - (m - 1) * (v2 - v1) * v2)
    return x / v2 + (l - x) / v1
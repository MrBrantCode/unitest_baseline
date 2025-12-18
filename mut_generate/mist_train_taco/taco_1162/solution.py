"""
QUESTION:
The start of the new academic year brought about the problem of accommodation students into dormitories. One of such dormitories has a a × b square meter wonder room. The caretaker wants to accommodate exactly n students there. But the law says that there must be at least 6 square meters per student in a room (that is, the room for n students must have the area of at least 6n square meters). The caretaker can enlarge any (possibly both) side of the room by an arbitrary positive integer of meters. Help him change the room so as all n students could live in it and the total area of the room was as small as possible.


-----Input-----

The first line contains three space-separated integers n, a and b (1 ≤ n, a, b ≤ 10^9) — the number of students and the sizes of the room.


-----Output-----

Print three integers s, a_1 and b_1 (a ≤ a_1; b ≤ b_1) — the final area of the room and its sizes. If there are multiple optimal solutions, print any of them.


-----Examples-----
Input
3 3 5

Output
18
3 6

Input
2 4 4

Output
16
4 4
"""

from math import ceil

def calculate_optimal_room_dimensions(n, a, b):
    s = 6 * n
    if a * b >= s:
        a_1, b_1 = a, b
    else:
        a1, b1 = min(a, b), max(a, b)
        q = [(x, ceil(s / x)) for x in range(a1, ceil(s ** 0.5)) if ceil(s / x) > b1]
        if q:
            x, y = min(q, key=lambda c: c[0] * c[1])
        else:
            x, y = a1, ceil(s / a1)
        if x < a:
            x, y = y, x
        a_1, b_1 = x, y
    return s, a_1, b_1
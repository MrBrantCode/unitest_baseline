"""
QUESTION:
Salve, mi amice.

Et tu quidem de lapis philosophorum. Barba non facit philosophum. Labor omnia vincit. Non potest creatio ex nihilo. Necesse est partibus.

Rp:

    I Aqua Fortis

    I Aqua Regia

    II Amalgama

    VII Minium

    IV Vitriol

Misce in vitro et æstus, et nil admirari. Festina lente, et nulla tenaci invia est via.

Fac et spera,

Vale,

Nicolas Flamel


-----Input-----

The first line of input contains several space-separated integers a_{i} (0 ≤ a_{i} ≤ 100).


-----Output-----

Print a single integer.


-----Examples-----
Input
2 4 6 8 10

Output
1
"""

def calculate_minimum_reactions(a: list[int]) -> int:
    b = [1, 1, 2, 7, 4]
    for i in range(len(a)):
        a[i] = a[i] // b[i]
    return min(a)
"""
QUESTION:
Mad scientist Mike is busy carrying out experiments in chemistry. Today he will attempt to join three atoms into one molecule.

A molecule consists of atoms, with some pairs of atoms connected by atomic bonds. Each atom has a valence number — the number of bonds the atom must form with other atoms. An atom can form one or multiple bonds with any other atom, but it cannot form a bond with itself. The number of bonds of an atom in the molecule must be equal to its valence number. [Image] 

Mike knows valence numbers of the three atoms. Find a molecule that can be built from these atoms according to the stated rules, or determine that it is impossible.


-----Input-----

The single line of the input contains three space-separated integers a, b and c (1 ≤ a, b, c ≤ 10^6) — the valence numbers of the given atoms.


-----Output-----

If such a molecule can be built, print three space-separated integers — the number of bonds between the 1-st and the 2-nd, the 2-nd and the 3-rd, the 3-rd and the 1-st atoms, correspondingly. If there are multiple solutions, output any of them. If there is no solution, print "Impossible" (without the quotes).


-----Examples-----
Input
1 1 2

Output
0 1 1

Input
3 4 5

Output
1 3 2

Input
4 1 1

Output
Impossible



-----Note-----

The first sample corresponds to the first figure. There are no bonds between atoms 1 and 2 in this case.

The second sample corresponds to the second figure. There is one or more bonds between each pair of atoms.

The third sample corresponds to the third figure. There is no solution, because an atom cannot form bonds with itself.

The configuration in the fourth figure is impossible as each atom must have at least one atomic bond.
"""

def build_molecule(a: int, b: int, c: int) -> str or tuple:
    # Check if the sum of valences is odd or if any atom's valence is greater than the sum of the other two
    if (a + b + c) % 2 == 1 or max(a, b, c) > (a + b + c) - max(a, b, c):
        return "Impossible"
    
    # Check if all valences are the same
    if a == b == c:
        return (a // 2, a // 2, a // 2)
    
    # Check if two atoms have the same minimum valence
    if a == b or b == c or a == c:
        min_val = min(a, b, c)
        max_val = max(a, b, c)
        if a == min_val and b == min_val:
            return (max_val // 2, (min_val * 2 - max_val) // 2, max_val // 2)
        elif b == min_val and c == min_val:
            return ((min_val * 2 - max_val) // 2, max_val // 2, max_val // 2)
        elif a == min_val and c == min_val:
            return (max_val // 2, max_val // 2, (min_val * 2 - max_val) // 2)
    
    # General case for different valences
    total_sum = a + b + c
    half_sum = total_sum // 2
    
    if min(a, b, c) == a:
        return (b - half_sum + a, half_sum - a, c - half_sum + a)
    elif min(a, b, c) == b:
        return (a - half_sum + b, c - half_sum + b, half_sum - b)
    elif min(a, b, c) == c:
        return (half_sum - c, b - half_sum + c, a - half_sum + c)
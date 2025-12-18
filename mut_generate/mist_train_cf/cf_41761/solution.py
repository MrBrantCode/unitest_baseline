"""
QUESTION:
Implement the `germinate` function to generate a set of permutations by repeatedly applying inverse and composition operations to the input set. The function takes a set of permutations `subset` as input and returns the updated set. You need to implement the composition of permutations in the `germinate` function. 

The `germinate` function should take a set of permutations `subset` as input and return a set of permutations. The function should repeatedly apply the inverse and composition operations to the input set until no new permutations are added. The composition of two permutations `p1` and `p2` should be implemented in the `compose` function.

Restrictions: The input set `subset` is a set of permutations, and the output should be a set of permutations. The `germinate` function should continue applying the inverse and composition operations until no new permutations are added to the set.
"""

from typing import Set, Tuple

def compose(p1: Tuple[int, ...], p2: Tuple[int, ...]) -> Tuple[int, ...]:
    composed_permutation = tuple(p1[p2[i]] for i in range(len(p1)))
    return composed_permutation

def germinate(subset: Set[Tuple[int, ...]]) -> Set[Tuple[int, ...]]:
    while True:
        n = len(subset)
        subset = subset.union([tuple(reversed(p)) for p in subset])
        new_permutations = set()
        for p1 in subset:
            for p2 in subset:
                new_permutations.add(compose(p1, p2))
        subset = subset.union(new_permutations)
        if len(subset) == n:
            break
    return subset
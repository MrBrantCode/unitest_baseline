"""
QUESTION:
Recently Max has got himself into popular CCG "BrainStone". As "BrainStone" is a pretty intellectual game, Max has to solve numerous hard problems during the gameplay. Here is one of them:

Max owns n creatures, i-th of them can be described with two numbers — its health hp_{i} and its damage dmg_{i}. Max also has two types of spells in stock:  Doubles health of the creature (hp_{i} := hp_{i}·2);  Assigns value of health of the creature to its damage (dmg_{i} := hp_{i}). 

Spell of first type can be used no more than a times in total, of the second type — no more than b times in total. Spell can be used on a certain creature multiple times. Spells can be used in arbitrary order. It isn't necessary to use all the spells.

Max is really busy preparing for his final exams, so he asks you to determine what is the maximal total damage of all creatures he can achieve if he uses spells in most optimal way.


-----Input-----

The first line contains three integers n, a, b (1 ≤ n ≤ 2·10^5, 0 ≤ a ≤ 20, 0 ≤ b ≤ 2·10^5) — the number of creatures, spells of the first type and spells of the second type, respectively.

The i-th of the next n lines contain two number hp_{i} and dmg_{i} (1 ≤ hp_{i}, dmg_{i} ≤ 10^9) — description of the i-th creature.


-----Output-----

Print single integer — maximum total damage creatures can deal.


-----Examples-----
Input
2 1 1
10 15
6 1

Output
27

Input
3 0 3
10 8
7 11
5 2

Output
26



-----Note-----

In the first example Max should use the spell of the first type on the second creature, then the spell of the second type on the same creature. Then total damage will be equal to 15 + 6·2 = 27.

In the second example Max should use the spell of the second type on the first creature, then the spell of the second type on the third creature. Total damage will be equal to 10 + 11 + 5 = 26.
"""

def calculate_max_total_damage(n, a, b, creatures):
    def bdiff(creature):
        return max(0, creature[0] - creature[1])

    # Calculate the initial total damage without any spells
    ans = sum(creature[1] for creature in creatures)

    if b == 0:
        return ans

    # Sort creatures based on the difference bdiff
    creatures.sort(key=bdiff)

    best = 0
    if n > b:
        lost = bdiff(creatures[n - b])
        for creature in creatures[:n - b]:
            best = max(best, (creature[0] << a) - creature[1] - lost)

    for creature in creatures[max(0, n - b):]:
        best = max(best, (creature[0] << a) - max(creature))
        ans += bdiff(creature)

    ans += best
    return ans
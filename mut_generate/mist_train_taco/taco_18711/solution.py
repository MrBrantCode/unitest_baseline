"""
QUESTION:
Vova plays a computer game known as Mages and Monsters. Vova's character is a mage. Though as he has just started, his character knows no spells.

Vova's character can learn new spells during the game. Every spell is characterized by two values x_{i} and y_{i} — damage per second and mana cost per second, respectively. Vova doesn't have to use a spell for an integer amount of seconds. More formally, if he uses a spell with damage x and mana cost y for z seconds, then he will deal x·z damage and spend y·z mana (no rounding). If there is no mana left (mana amount is set in the start of the game and it remains the same at the beginning of every fight), then character won't be able to use any spells. It is prohibited to use multiple spells simultaneously.

Also Vova can fight monsters. Every monster is characterized by two values t_{j} and h_{j} — monster kills Vova's character in t_{j} seconds and has h_{j} health points. Mana refills after every fight (or Vova's character revives with full mana reserve), so previous fights have no influence on further ones.

Vova's character kills a monster, if he deals h_{j} damage to it in no more than t_{j} seconds using his spells (it is allowed to use more than one spell in a fight) and spending no more mana than he had at the beginning of the fight. If monster's health becomes zero exactly in t_{j} seconds (it means that the monster and Vova's character kill each other at the same time), then Vova wins the fight.

You have to write a program which can answer two types of queries:

  1 x y — Vova's character learns new spell which deals x damage per second and costs y mana per second.  2 t h — Vova fights the monster which kills his character in t seconds and has h health points. 

Note that queries are given in a different form. Also remember that Vova's character knows no spells at the beginning of the game.

For every query of second type you have to determine if Vova is able to win the fight with corresponding monster.


-----Input-----

The first line contains two integer numbers q and m (2 ≤ q ≤ 10^5, 1 ≤ m ≤ 10^12) — the number of queries and the amount of mana at the beginning of every fight.

i-th of each next q lines contains three numbers k_{i}, a_{i} and b_{i} (1 ≤ k_{i} ≤ 2, 1 ≤ a_{i}, b_{i} ≤ 10^6). 

Using them you can restore queries this way: let j be the index of the last query of second type with positive answer (j = 0 if there were none of these).   If k_{i} = 1, then character learns spell with x = (a_{i} + j) mod 10^6 + 1, y = (b_{i} + j) mod 10^6 + 1.  If k_{i} = 2, then you have to determine if Vova is able to win the fight against monster with t = (a_{i} + j) mod 10^6 + 1, h = (b_{i} + j) mod 10^6 + 1. 


-----Output-----

For every query of second type print YES if Vova is able to win the fight with corresponding monster and NO otherwise.


-----Example-----
Input
3 100
1 4 9
2 19 49
2 19 49

Output
YES
NO



-----Note-----

In first example Vova's character at first learns the spell with 5 damage and 10 mana cost per second. Next query is a fight with monster which can kill character in 20 seconds and has 50 health points. Vova kills it in 10 seconds (spending 100 mana). Next monster has 52 health, so Vova can't deal that much damage with only 100 mana.
"""

def can_vova_win(queries, mana):
    mod = 10 ** 6
    j = 0
    spell_chull = [(0, 0)]

    def is_right(xy0, xy1, xy):
        (x0, y0) = xy0
        (x1, y1) = xy1
        (x, y) = xy
        return (x0 - x) * (y1 - y) >= (x1 - x) * (y0 - y)

    def in_chull(x, y):
        i = 0
        if x > spell_chull[-1][0]:
            return False
        while spell_chull[i][0] < x:
            i += 1
        if spell_chull[i][0] == x:
            return spell_chull[i][1] <= y
        else:
            return is_right(spell_chull[i - 1], spell_chull[i], (x, y))

    def add_spell(x, y):
        nonlocal spell_chull
        if in_chull(x, y):
            return
        i_left = 0
        while i_left < len(spell_chull) - 1 and (not is_right(spell_chull[i_left + 1], spell_chull[i_left], (x, y))):
            i_left += 1
        i_right = i_left + 1
        while i_right < len(spell_chull) - 1 and is_right(spell_chull[i_right + 1], spell_chull[i_right], (x, y)):
            i_right += 1
        if i_right == len(spell_chull) - 1 and x >= spell_chull[-1][0]:
            i_right += 1
        spell_chull = spell_chull[:i_left + 1] + [(x, y)] + spell_chull[i_right:]

    results = []
    for (i, qi) in enumerate(queries):
        (k, a, b) = qi
        x = (a + j) % mod + 1
        y = (b + j) % mod + 1
        if k == 1:
            add_spell(x, y)
        elif in_chull(y / x, mana / x):
            results.append('YES')
            j = i + 1
        else:
            results.append('NO')
    
    return results
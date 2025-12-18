"""
QUESTION:
Recently, Petya learned about a new game "Slay the Dragon". As the name suggests, the player will have to fight with dragons. To defeat a dragon, you have to kill it and defend your castle. To do this, the player has a squad of $n$ heroes, the strength of the $i$-th hero is equal to $a_i$.

According to the rules of the game, exactly one hero should go kill the dragon, all the others will defend the castle. If the dragon's defense is equal to $x$, then you have to send a hero with a strength of at least $x$ to kill it. If the dragon's attack power is $y$, then the total strength of the heroes defending the castle should be at least $y$.

The player can increase the strength of any hero by $1$ for one gold coin. This operation can be done any number of times.

There are $m$ dragons in the game, the $i$-th of them has defense equal to $x_i$ and attack power equal to $y_i$. Petya was wondering what is the minimum number of coins he needs to spend to defeat the $i$-th dragon.

Note that the task is solved independently for each dragon (improvements are not saved).


-----Input-----

The first line contains a single integer $n$ ($2 \le n \le 2 \cdot 10^5$) — number of heroes.

The second line contains $n$ integers $a_1, a_2, \dots, a_n$ ($1 \le a_i \le 10^{12}$), where $a_i$ is the strength of the $i$-th hero.

The third line contains a single integer $m$ ($1 \le m \le 2 \cdot 10^5$) — the number of dragons.

The next $m$ lines contain two integers each, $x_i$ and $y_i$ ($1 \le x_i \le 10^{12}; 1 \le y_i \le 10^{18}$) — defense and attack power of the $i$-th dragon.


-----Output-----

Print $m$ lines, $i$-th of which contains a single integer — the minimum number of coins that should be spent to defeat the $i$-th dragon.


-----Examples-----

Input
4
3 6 2 3
5
3 12
7 9
4 14
1 10
8 7
Output
1
2
4
0
2


-----Note-----

To defeat the first dragon, you can increase the strength of the third hero by $1$, then the strength of the heroes will be equal to $[3, 6, 3, 3]$. To kill the dragon, you can choose the first hero.

To defeat the second dragon, you can increase the forces of the second and third heroes by $1$, then the strength of the heroes will be equal to $[3, 7, 3, 3]$. To kill the dragon, you can choose a second hero.

To defeat the third dragon, you can increase the strength of all the heroes by $1$, then the strength of the heroes will be equal to $[4, 7, 3, 4]$. To kill the dragon, you can choose a fourth hero.

To defeat the fourth dragon, you don't need to improve the heroes and choose a third hero to kill the dragon.

To defeat the fifth dragon, you can increase the strength of the second hero by $2$, then the strength of the heroes will be equal to $[3, 8, 2, 3]$. To kill the dragon, you can choose a second hero.
"""

from bisect import bisect_left, bisect_right
from math import inf

def calculate_min_coins(hero_strengths, dragon_defenses, dragon_attacks):
    # Sort the hero strengths and calculate the total strength
    hero_strengths.sort()
    total_strength = sum(hero_strengths)
    
    # Initialize the result list
    min_coins_needed = []
    
    # Iterate over each dragon
    for x, y in zip(dragon_defenses, dragon_attacks):
        # Find the indices for potential heroes to fight the dragon
        index1 = bisect_left(hero_strengths, x + 1) - 1
        index2 = bisect_right(hero_strengths, x)
        
        # Initialize the minimum coins needed to a large number
        mini = inf
        
        # Check the first potential hero
        if 0 <= index1 < len(hero_strengths):
            tot1 = total_strength - hero_strengths[index1]
            req1 = max(0, x - hero_strengths[index1])
            req2 = max(0, y - tot1)
            mini = min(mini, req1 + req2)
        
        # Check the second potential hero
        if index2 < len(hero_strengths):
            tot1 = total_strength - hero_strengths[index2]
            req = max(0, y - tot1)
            mini = min(mini, req)
        
        # Append the minimum coins needed for this dragon to the result list
        min_coins_needed.append(mini)
    
    return min_coins_needed
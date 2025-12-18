"""
QUESTION:
Read problem statements in [Bengali], [Mandarin Chinese], [Russian], and [Vietnamese] as well.

Chef and $N-1$ more of his friends go to the night canteen. The canteen serves only three items (well, they serve more, but only these three are edible!), which are omelette, chocolate milkshake, and chocolate cake. Their prices are $A$, $B$ and $C$ respectively.

However, the canteen is about to run out of some ingredients. In particular, they only have $E$ eggs and $H$ chocolate bars left. They need:
$2$ eggs to make an omelette
$3$ chocolate bars for a chocolate milkshake
$1$ egg and $1$ chocolate bar for a chocolate cake

Each of the $N$ friends wants to order one item. They can only place an order if the canteen has enough ingredients to prepare all the ordered items. Find the smallest possible total price they have to pay or determine that it is impossible to prepare $N$ items.

------  Input ------
The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
The first and only line of each test case contains six space-separated integers $N$, $E$, $H$, $A$, $B$ and $C$.

------  Output ------
For each test case, print a single line containing one integer ― the minimum cost of $N$ items, or $-1$ if it is impossible to prepare $N$ items.

------  Constraints ------
$1 ≤ T ≤ 2 \cdot 10^{5}$
$1 ≤ N ≤ 10^{6}$
$0 ≤ E, H ≤ 10^{6}$
$1 ≤ A, B, C ≤ 10^{6}$
the sum of $N$ over all test cases does not exceed $10^{6}$

------  Subtasks ------
Subtask #1 (30 points): $1 ≤ N ≤ 100$

Subtask #2 (70 points): original constraints

----- Sample Input 1 ------ 
3

5 4 4 2 2 2

4 5 5 1 2 3

4 5 5 3 2 1
----- Sample Output 1 ------ 
-1

7

4
----- explanation 1 ------ 
Example case 1: The maximum number of items that can be produced using $4$ eggs and $4$ chocolates is $4$, so the answer is $-1$.

Example case 2: In the optimal solution, the friends should order $2$ omelettes, $1$ chocolate milkshake and $1$ chocolate cake, with cost $1 \cdot 2 + 2 \cdot 1 + 3 \cdot 1 = 7$.

Example case 3: In the optimal solution, the friends should order $4$ chocolate cakes, with cost $1 \cdot 4 = 4$.
"""

from math import inf

def calculate_minimum_cost(N, E, H, A, B, C):
    min_cost = inf
    
    for chocolate_cake in range(min(N, min(E, H)) + 1):
        total_cost = chocolate_cake * C
        remaining = N - chocolate_cake
        egg = max(0, E - chocolate_cake)
        choco_bar = max(0, H - chocolate_cake)
        
        if A < B:
            total_cost += min(egg // 2, remaining) * A
            remaining -= min(egg // 2, remaining)
            total_cost += min(choco_bar // 3, remaining) * B
            remaining -= min(choco_bar // 3, remaining)
        else:
            total_cost += min(choco_bar // 3, remaining) * B
            remaining -= min(choco_bar // 3, remaining)
            total_cost += min(egg // 2, remaining) * A
            remaining -= min(egg // 2, remaining)
        
        if not remaining:
            min_cost = min(min_cost, total_cost)
    
    return -1 if min_cost == inf else min_cost
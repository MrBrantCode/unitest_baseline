"""
QUESTION:
Vasya plays one very well-known and extremely popular MMORPG game. His game character has k skill; currently the i-th of them equals to ai. Also this game has a common rating table in which the participants are ranked according to the product of all the skills of a hero in the descending order.

Vasya decided to 'upgrade' his character via the game store. This store offers n possible ways to improve the hero's skills; Each of these ways belongs to one of three types:

  1. assign the i-th skill to b; 
  2. add b to the i-th skill; 
  3. multiply the i-th skill by b. 



Unfortunately, a) every improvement can only be used once; b) the money on Vasya's card is enough only to purchase not more than m of the n improvements. Help Vasya to reach the highest ranking in the game. To do this tell Vasya which of improvements he has to purchase and in what order he should use them to make his rating become as high as possible. If there are several ways to achieve it, print any of them.

Input

The first line contains three numbers — k, n, m (1 ≤ k ≤ 105, 0 ≤ m ≤ n ≤ 105) — the number of skills, the number of improvements on sale and the number of them Vasya can afford.

The second line contains k space-separated numbers ai (1 ≤ ai ≤ 106), the initial values of skills.

Next n lines contain 3 space-separated numbers tj, ij, bj (1 ≤ tj ≤ 3, 1 ≤ ij ≤ k, 1 ≤ bj ≤ 106) — the type of the j-th improvement (1 for assigning, 2 for adding, 3 for multiplying), the skill to which it can be applied and the value of b for this improvement.

Output

The first line should contain a number l (0 ≤ l ≤ m) — the number of improvements you should use.

The second line should contain l distinct space-separated numbers vi (1 ≤ vi ≤ n) — the indices of improvements in the order in which they should be applied. The improvements are numbered starting from 1, in the order in which they appear in the input. 

Examples

Input

2 4 3
13 20
1 1 14
1 2 30
2 1 6
3 2 2


Output

3
2 3 4
"""

def maximize_hero_rating(k, n, m, initial_skills, improvements):
    # Initialize the list of improvements for each skill
    l = [[[], [], []] for _ in range(k)]
    
    # Populate the list with improvements
    for j, (t, i, b) in enumerate(improvements):
        l[i - 1][t - 1].append((b, j + 1))
    
    # Sort the improvements in descending order for each type
    for i in range(k):
        for j in range(3):
            l[i][j].sort(reverse=True)
    
    op = []
    for i in range(k):
        t = l[i][1][:]
        if l[i][0] and l[i][0][0][0] > initial_skills[i]:
            t.append((l[i][0][0][0] - initial_skills[i], l[i][0][0][1]))
            t.sort(reverse=True)
        s = initial_skills[i]
        for add, index in t:
            op.append(((s + add) / s, index))
            s += add
        for mul, index in l[i][2]:
            op.append((mul, index))
    
    # Sort the operations in descending order of their impact
    op.sort(reverse=True)
    
    # Select the top m improvements
    st = set(map(lambda t: t[1], op[:m]))
    
    # Collect the indices of the selected improvements
    improvement_indices = []
    for i in range(k):
        for j in range(3):
            for mul, index in l[i][j]:
                if index in st:
                    improvement_indices.append(index)
    
    return len(st), improvement_indices
"""
QUESTION:
Vasilisa the Wise from a far away kingdom got a present from her friend Helga the Wise from a farther away kingdom. The present is a surprise box, yet Vasilisa the Wise doesn't know yet what the surprise actually is because she cannot open the box. She hopes that you can help her in that.

The box's lock is constructed like that. The box itself is represented by an absolutely perfect black cube with the identical deepening on each face (those are some foreign nanotechnologies that the far away kingdom scientists haven't dreamt of). The box is accompanied by six gems whose form matches the deepenings in the box's faces. The box can only be opened after it is correctly decorated by the gems, that is, when each deepening contains exactly one gem. Two ways of decorating the box are considered the same if they can be obtained one from the other one by arbitrarily rotating the box (note that the box is represented by a perfect nanotechnological cube)

Now Vasilisa the Wise wants to know by the given set of colors the following: in how many ways would she decorate the box in the worst case to open it? To answer this question it is useful to know that two gems of one color are indistinguishable from each other. Help Vasilisa to solve this challenging problem.

Input

The first line contains exactly 6 characters without spaces from the set {R, O, Y, G, B, V} — they are the colors of gems with which the box should be decorated.

Output

Print the required number of different ways to decorate the box.

Examples

Input

YYYYYY


Output

1


Input

BOOOOB


Output

2


Input

ROYGBV


Output

30
"""

from functools import reduce

def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))

def calculate_unique_decorations(gem_colors):
    colors = {'R': 0, 'O': 0, 'Y': 0, 'G': 0, 'B': 0, 'V': 0}
    for c in gem_colors:
        colors[c] += 1
    
    amount = list(reversed(sorted([(colors[key], key) for key in colors])))
    amount = [x[0] for x in amount]
    
    if amount[0] == 6 or amount[0] == 5:
        return 1
    elif amount[0] == 4:
        return 2
    elif amount[0] == 3:
        if amount[1] == 3:
            return 2
        elif amount[1] == 2:
            return 3
        elif amount[1] == 1:
            return 5
    elif amount[0] == 2:
        if amount[1] == amount[2] == 2:
            return 6
        elif amount[1] == 2:
            return 8
        else:
            return factorial(6) // 48
    elif amount[0] == 1:
        return factorial(6) // 24
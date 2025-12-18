"""
QUESTION:
The Rebel fleet is afraid that the Empire might want to strike back again. Princess Heidi needs to know if it is possible to assign R Rebel spaceships to guard B bases so that every base has exactly one guardian and each spaceship has exactly one assigned base (in other words, the assignment is a perfect matching). Since she knows how reckless her pilots are, she wants to be sure that any two (straight) paths – from a base to its assigned spaceship – do not intersect in the galaxy plane (that is, in 2D), and so there is no risk of collision.


-----Input-----

The first line contains two space-separated integers R, B(1 ≤ R, B ≤ 10). For 1 ≤ i ≤ R, the i + 1-th line contains two space-separated integers x_{i} and y_{i} (|x_{i}|, |y_{i}| ≤ 10000) denoting the coordinates of the i-th Rebel spaceship. The following B lines have the same format, denoting the position of bases. It is guaranteed that no two points coincide and that no three points are on the same line.


-----Output-----

If it is possible to connect Rebel spaceships and bases so as satisfy the constraint, output Yes, otherwise output No (without quote).


-----Examples-----
Input
3 3
0 0
2 0
3 1
-2 1
0 3
2 2

Output
Yes

Input
2 1
1 0
2 2
3 1

Output
No



-----Note-----

For the first example, one possible way is to connect the Rebels and bases in order.

For the second example, there is no perfect matching between Rebels and bases.
"""

def is_perfect_matching_possible(R, B, spaceships, bases):
    def check(a, b):
        ansa = b[0] - a[0]
        ansb = b[1] - a[1]
        return [ansa, ansb]
    
    if R != B:
        return False
    
    for i in range(len(spaceships)):
        for j in range(i + 1, len(spaceships)):
            for k in range(len(bases)):
                for l in range(k + 1, len(bases)):
                    ansa = check(spaceships[i], spaceships[j])
                    ansb = check(spaceships[i], bases[k])
                    ansc = check(spaceships[i], bases[l])
                    if (ansa[0] == ansb[0] and ansa[0] == ansc[0] and (ansa[0] == 0)) or \
                       (ansa[0] != 0 and ansb[0] != 0 and ansc[0] != 0 and \
                        (ansa[1] / ansa[0] == ansb[1] / ansb[0]) and \
                        (ansa[1] / ansa[0] == ansc[1] / ansc[0])):
                        return False
    return True
"""
QUESTION:
To almost all of us solving sets of linear equations is quite obviously the most exciting bit of linear algebra. Benny does not agree though and wants to write a quick program to solve his homework problems for him. Unfortunately Benny's lack of interest in linear algebra means he has no real clue on how to go about this. Fortunately, you can help him!

Write a method ```solve``` that accepts a list of linear equations that your method will have to solve. The output should be a map (a `Map` object in JavaScript) with a value for each variable in the equations. If the system does not have a unique solution (has infinitely many solutions or is unsolvable), return ```null``` (`None` in python).

For example :  
  
"2x + 4y + 6z = 18"  
"3y + 3z = 6"  
"x + 2y = z - 3"
  
should result in a map :  
  
x = 2  
y = -1  
z = 3  
  
Possible input equations have the following rules:  
-   Only the plus and minus operators are used on both the left and right hand side of the equation.  
-   Both sides of the equation can have variables; One variable can appear in multiple terms, on both sides.
-   Variable names are strings of arbitrary length.  
-   All coefficients are integers and generally fall within the range of -150 to 150, with a few ranging from -1000 to 1000. Free terms are integers in range -20000 to 20000.  
-   Equations do not necessarily have variables.  
-   Equations have exactly one operator (+ or -) between terms.  


Comparisons are performed with accuracy of `1e-6`.

**Note on numerical stability:**

There are many possible ways to solve a system of linear equations. One group of such algorithms is based on reduction and elimination methods. If you are going to use any of these, remember that such algorithms are in general *numerically unstable*, i.e. division operations repeated over and over introduce inaccuracies which accumulate from row to row. As a result it might occur that some value which is expected to be zero is actually larger, for example, `2.5e-10`. Such inaccuracies tend to be bigger in large equation systems, and random tests check systems of up to 26 equations. If it happens that small tests pass for you, and large tests fail, it probably means that you did not account for inaccuracies correctly.
Also note that tests do not depend on any reference solution, so the way how test cases are generated _is numrically stable_ - the only source of inaccuracies is your solution, and you need to account for it.

```if:python
___Note for python users:___

`numpy` module has been disabled, so that the task matches the one of the other languages. There is an anti-cheat measure about that, so you won't be able to import some other modules too (either way, you shouldn't need any module to solve this kata...)
```
"""

from collections import defaultdict
from functools import reduce
import re

P_EQ = re.compile('(?P<eq>=)|(?P<coef>[+-]?\\d*)(?P<var>[a-zA-Z]*)')

def solve_linear_equations(equations):
    def parse(eq):
        (rev, dct) = (1, defaultdict(int))
        for m in P_EQ.finditer(eq.replace(' ', '')):
            if m['eq']:
                rev = -1
            else:
                (gc, gv) = (m['coef'], m['var'])
                if gc or gv:
                    coef = 1 if not gc or gc == '+' else -1 if gc == '-' else int(gc)
                    dct[m['var']] += coef * rev
        return dct

    def solveMatrix(m, vars):
        EPS = 1e-10
        pivots = {}
        toDo = set(range(len(m)))
        for y in range(len(vars) - 1):
            (_, px) = max(((abs(m[x][y]), x) for x in toDo if abs(m[x][y]) > 0), default=(-1, -1))
            if px == -1:
                continue
            pivots[px] = y
            toDo.remove(px)
            (maxP, m[px][y]) = (m[px][y], 1)
            for j in range(y + 1, len(vars)):
                m[px][j] /= maxP
                if abs(m[px][j]) < EPS:
                    m[px][j] = 0
            for x in range(0, len(m)):
                if x == px:
                    continue
                (coef, m[x][y]) = (m[x][y], 0)
                for j in range(y + 1, len(vars)):
                    m[x][j] -= coef * m[px][j]
                    if abs(m[x][j]) < EPS:
                        m[x][j] = 0
        solvedDct = {}
        for x in range(len(m)):
            yP = pivots.get(x, None)
            if yP is None:
                continue
            solvedDct[vars[yP]] = -m[x][-1]
        if len(solvedDct) == len(vars) - 1:
            return solvedDct

    eqsMap = list(map(parse, equations))
    vars = reduce(set.union, (set(e) for e in eqsMap))
    vars = list(set(vars) - {''}) + ['']
    if len(vars) - 1 > len(equations):
        return None
    m = [[eqm[v] for v in vars] for eqm in eqsMap]
    return solveMatrix(m, vars)
"""
QUESTION:
This problem was part of the CodeChef April Challenge.  All user submissions for this contest problem are publicly available here.

In the game of "BattleShip V", you control a cannon which is attacking a large enemy battleship, armed with many guns. Your goal is to destroy as many of the guns as possible.
The battle field is a 2D Cartesian grid, where your cannon is located at the origin.
The enemy battleship is a horizontal line segment located from the coordinates (X1 , Y) to (X2, Y). 
There are exactly (X2 - X1 + 1) guns on the ship, located at the integer points (X1, Y), (X1+1, Y), ..., (X2, Y).

However, the problem is, you cannot always fire at a gun. There are supernatural rocks located at all points of the battlefield whose X and Y coordinates are both integers. In order to fire successfully at an enemy's gun, the line connecting your cannon and that gun must not 
go through any rocks.

How many guns you successfully destroy?

------ Input ------ 

The first line contains t, the number of test cases (about 100). Then t test cases follow.

Each test case consists of one line containing three numbers Y, and X1, X2 (0 < |Y| ≤ 2100000000, -2100000000 ≤ X _{1} ≤ X_{2} ≤ 2100000000).

------ Output ------ 

For each test case, output the number of the enemy battleship's guns that your cannon can destroy.

----- Sample Input 1 ------ 
1
2 -2 1
----- Sample Output 1 ------ 
2
"""

def factorize(y):
    z = []
    x = 2
    while x * x <= y:
        if y % x == 0:
            z.append(x)
            while y % x == 0:
                y //= x
        x += 1
    if y > 1:
        z.append(y)
    return z

def CoprimeCount(fact, x):
    k = len(fact)
    Net = 1 << k
    ans = 0
    for mask in range(Net):
        cnt = 0
        val = 1
        for i in range(k):
            if 1 << i & mask != 0:
                val *= fact[i]
                cnt += 1
        if cnt & 1 == 1:
            ans -= x // val
        else:
            ans += x // val
    return ans

def count_destroyed_guns(y, x1, x2):
    y = abs(y)
    if y == 1:
        if x1 * x2 <= 0:
            return abs(x1) + abs(x2) + 1
        else:
            return abs(x2 - x1) + 1
    if y == 0:
        if x1 < 0 and x2 > 0:
            return 3
        elif (x1 == 0 and x2 > 0) or (x1 < 0 and x2 == 0):
            return 2
        else:
            return 1
    
    fact = factorize(y)
    ans = 0
    if x1 * x2 < 0:
        ans += CoprimeCount(fact, abs(x1))
        ans += CoprimeCount(fact, abs(x2))
    else:
        if x1 <= 0 and x2 <= 0:
            x1, x2 = -x2, -x1
        ans += CoprimeCount(fact, x2)
        ans -= CoprimeCount(fact, max(0, x1 - 1))
    
    return ans
"""
QUESTION:
Dee Dee went to market to buy some eggs. There are 2 type of egg cartons available in the shop. One type contains 6 eggs and the other type contains 8 eggs. Dee Dee wants to buy exactly N eggs. Calculate the minimal number of egg cartons she must buy.

INPUT

First line of input gives T, the number of test cases.
T lines follow, each having N, the number of eggs.

OUTPUT

Print the minimal number of egg cartons she must buy.
If it's impossible to buy exactly n eggs, print -1.

CONSTRAINTS
1 ≤ T ≤ 50
1 ≤ N ≤ 100

SAMPLE INPUT
2
20
24

SAMPLE OUTPUT
3
3

Explanation

For first case, she should buy 2 cartons containing 6 eggs and 1 carton containing 8 eggs. In total, she buys 3 egg cartons.
For second case, there are two ways to buy 24 eggs: buy 4 cartons containing 6 eggs or buy 3 cartons containing 8 eggs. Minimize the number of cartons.
"""

def minimal_egg_cartons(N):
    eights = 0
    sixs = 0
    qty = N
    
    while qty > 5:
        if qty % 8 == 0:
            eights += 1
            qty -= 8
        else:
            sixs += 1
            qty -= 6
    
    if eights * 8 + sixs * 6 == N:
        return eights + sixs
    else:
        return -1
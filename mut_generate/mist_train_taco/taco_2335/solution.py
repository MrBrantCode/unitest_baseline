"""
QUESTION:
This is an easy version of the problem. In this version, all cards have the same color.

Alice has $n$ cards, each card is white, and the cards are stacked in a deck. Alice deals the cards to herself and to Bob, dealing at once several cards from the top of the deck in the following order: one card to herself, two cards to Bob, three cards to Bob, four cards to herself, five cards to herself, six cards to Bob, seven cards to Bob, eight cards to herself, and so on. In other words, on the $i$-th step, Alice deals $i$ top cards from the deck to one of the players; on the first step, she deals the cards to herself and then alternates the players every two steps. When there aren't enough cards at some step, Alice deals all the remaining cards to the current player, and the process stops.

First Alice's steps in a deck of many cards.

How many cards will Alice and Bob have at the end?


-----Input-----

Each test contains multiple test cases. The first line contains the number of test cases $t$ ($1 \le t \le 200$). The description of the test cases follows

The only line of each test case contains a single integer $n$ ($1 \le n \le 10^6$) — the number of cards.


-----Output-----

For each test case print two integers — the number of cards in the end for each player — in this order: cards Alice has, cards Bob has.


-----Examples-----

Input
5
10
6
17
8
1000000
Output
5 5
1 5
10 7
3 5
500202 499798


-----Note-----

None
"""

import math

def distribute_cards(n):
    """
    Distributes cards between Alice and Bob according to the given rules.

    Parameters:
    n (int): The number of cards to distribute.

    Returns:
    tuple: A tuple containing the number of cards Alice and Bob have at the end.
    """
    k = math.floor((2 * n) ** (1 / 2))
    if k * (k + 1) > 2 * n:
        k -= 1
    
    a = 0
    b = 0
    
    if k % 4 in (1, 2):
        b += n - k * (k + 1) // 2
    else:
        a += n - k * (k + 1) // 2
    
    if k % 4 == 0:
        a += k * (k + 1) // 4
        b += k * (k + 1) // 4
    elif k % 4 == 1:
        a += k
        k -= 1
        a += k * (k + 1) // 4
        b += k * (k + 1) // 4
    elif k % 4 == 2:
        b += k
        a += k - 1
        k -= 2
        a += k * (k + 1) // 4
        b += k * (k + 1) // 4
    else:
        b += 2 * k - 1
        a += k - 2
        k -= 3
        a += k * (k + 1) // 4
        b += k * (k + 1) // 4
    
    return (a, b)
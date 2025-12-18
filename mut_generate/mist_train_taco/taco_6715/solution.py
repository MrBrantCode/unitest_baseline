"""
QUESTION:
"Duel!"

Betting on the lovely princess Claris, the duel between Tokitsukaze and Quailty has started.

There are $n$ cards in a row. Each card has two sides, one of which has color. At first, some of these cards are with color sides facing up and others are with color sides facing down. Then they take turns flipping cards, in which Tokitsukaze moves first. In each move, one should choose exactly $k$ consecutive cards and flip them to the same side, which means to make their color sides all face up or all face down. If all the color sides of these $n$ cards face the same direction after one's move, the one who takes this move will win.

Princess Claris wants to know who will win the game if Tokitsukaze and Quailty are so clever that they won't make mistakes.


-----Input-----

The first line contains two integers $n$ and $k$ ($1 \le k \le n \le 10^5$).

The second line contains a single string of length $n$ that only consists of $0$ and $1$, representing the situation of these $n$ cards, where the color side of the $i$-th card faces up if the $i$-th character is $1$, or otherwise, it faces down and the $i$-th character is $0$.


-----Output-----

Print "once again" (without quotes) if the total number of their moves can exceed $10^9$, which is considered a draw.

In other cases, print "tokitsukaze" (without quotes) if Tokitsukaze will win, or "quailty" (without quotes) if Quailty will win.

Note that the output characters are case-sensitive, and any wrong spelling would be rejected.


-----Examples-----
Input
4 2
0101

Output
quailty

Input
6 1
010101

Output
once again

Input
6 5
010101

Output
tokitsukaze

Input
4 1
0011

Output
once again



-----Note-----

In the first example, no matter how Tokitsukaze moves, there would be three cards with color sides facing the same direction after her move, and Quailty can flip the last card to this direction and win.

In the second example, no matter how Tokitsukaze moves, Quailty can choose the same card and flip back to the initial situation, which can allow the game to end in a draw.

In the third example, Tokitsukaze can win by flipping the leftmost five cards up or flipping the rightmost five cards down.

The fourth example can be explained in the same way as the second example does.
"""

def determine_duel_winner(n, k, cards):
    a = [0] + [int(c) for c in cards]
    l = [0] * (n + 1)
    r = [0] * (n + 1)
    
    l[1] = 1
    r[n] = n
    
    for i in range(2, n + 1):
        if a[i - 1] == a[i]:
            l[i] = l[i - 1]
        else:
            l[i] = i
        
        if a[n - i + 1] == a[n - i + 2]:
            r[n - i + 1] = r[n - i + 2]
        else:
            r[n - i + 1] = n - i + 1
    
    def win1():
        if n == k or r[k + 1] == n or l[n - k] == 1:
            return True
        for i in range(2, n - k + 1):
            if l[i - 1] == 1 and r[i + k] == n and (a[i - 1] == a[i + k]):
                return True
        return False
    
    def win2():
        if 2 * k < n:
            return False
        for i in range(2, n - k + 1):
            if l[i - 1] != 1 or r[i + k] != n:
                return False
        return True
    
    if win1():
        return "tokitsukaze"
    elif win2():
        return "quailty"
    else:
        return "once again"
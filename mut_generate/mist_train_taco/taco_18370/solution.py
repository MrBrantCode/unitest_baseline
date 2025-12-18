"""
QUESTION:
Andrew, Fedor and Alex are inventive guys. Now they invent the game with strings for two players.

Given a group of n non-empty strings. During the game two players build the word together, initially the word is empty. The players move in turns. On his step player must add a single letter in the end of the word, the resulting word must be prefix of at least one string from the group. A player loses if he cannot move.

Andrew and Alex decided to play this game k times. The player who is the loser of the i-th game makes the first move in the (i + 1)-th game. Guys decided that the winner of all games is the player who wins the last (k-th) game. Andrew and Alex already started the game. Fedor wants to know who wins the game if both players will play optimally. Help him.

Input

The first line contains two integers, n and k (1 ≤ n ≤ 105; 1 ≤ k ≤ 109).

Each of the next n lines contains a single non-empty string from the given group. The total length of all strings from the group doesn't exceed 105. Each string of the group consists only of lowercase English letters.

Output

If the player who moves first wins, print "First", otherwise print "Second" (without the quotes).

Examples

Input

2 3
a
b


Output

First


Input

3 1
a
b
c


Output

First


Input

1 2
ab


Output

Second
"""

def determine_winner(n, k, words):
    class Node:
        def __init__(self):
            self.end = False
            self.nxt = {}
            self.w = None
            self.l = None

        def __setitem__(self, i, x):
            self.nxt[i] = x

        def __getitem__(self, i):
            return self.nxt[i]

    def makeTrie(strs):
        root = Node()
        for s in strs:
            n = root
            for c in s:
                i = ord(c) - ord('a')
                n = n.nxt.setdefault(i, Node())
            n.end = True
        return root

    def getw(n):
        if n.w != None:
            return n.w
        if not n.nxt:
            res = False
        else:
            res = False
            for x in n.nxt:
                if not getw(n.nxt[x]):
                    res = True
        n.w = res
        return res

    def getl(n):
        if n.l != None:
            return n.l
        if not n.nxt:
            res = True
        else:
            res = False
            for x in n.nxt:
                if not getl(n.nxt[x]):
                    res = True
        n.l = res
        return res

    T = makeTrie(words)
    W = getw(T)
    L = getl(T)

    if not W:
        return 'Second'
    elif L:
        return 'First'
    else:
        return 'First' if k % 2 else 'Second'
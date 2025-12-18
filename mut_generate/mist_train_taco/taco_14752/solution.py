"""
QUESTION:
Andrew, Fedor and Alex are inventive guys. Now they invent the game with strings for two players.

Given a group of n non-empty strings. During the game two players build the word together, initially the word is empty. The players move in turns. On his step player must add a single letter in the end of the word, the resulting word must be prefix of at least one string from the group. A player loses if he cannot move.

Andrew and Alex decided to play this game k times. The player who is the loser of the i-th game makes the first move in the (i + 1)-th game. Guys decided that the winner of all games is the player who wins the last (k-th) game. Andrew and Alex already started the game. Fedor wants to know who wins the game if both players will play optimally. Help him.


-----Input-----

The first line contains two integers, n and k (1 ≤ n ≤ 10^5; 1 ≤ k ≤ 10^9).

Each of the next n lines contains a single non-empty string from the given group. The total length of all strings from the group doesn't exceed 10^5. Each string of the group consists only of lowercase English letters.


-----Output-----

If the player who moves first wins, print "First", otherwise print "Second" (without the quotes).


-----Examples-----
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

def determine_winner(n, k, strings):
    class Node:
        def __init__(self):
            self.children = [None] * 26
            self.isEnd = False
            self.win = False
            self.lose = False

    class Trie:
        def __init__(self):
            self.root = Node()

        def insert(self, key):
            cur = self.root
            for i in range(len(key)):
                if cur.children[ord(key[i]) - ord('a')] is None:
                    cur.children[ord(key[i]) - ord('a')] = Node()
                cur = cur.children[ord(key[i]) - ord('a')]
            cur.isEnd = True

        def search(self, key):
            cur = self.root
            for i in range(len(key)):
                if cur.children[ord(key[i]) - ord('a')] is None:
                    return False
                cur = cur.children[ord(key[i]) - ord('a')]
            return cur is not None and cur.isEnd

        def assignWin(self, cur):
            flag = True
            for i in range(26):
                if cur.children[i] is not None:
                    flag = False
                    self.assignWin(cur.children[i])
            if flag:
                cur.win = False
                cur.lose = True
            else:
                for i in range(26):
                    if cur.children[i] is not None:
                        cur.win = cur.win or not cur.children[i].win
                        cur.lose = cur.lose or not cur.children[i].lose

    t = Trie()
    for s in strings:
        t.insert(s)
    t.assignWin(t.root)

    if not t.root.win:
        return 'Second'
    elif t.root.lose:
        return 'First'
    elif k % 2 == 1:
        return 'First'
    else:
        return 'Second'
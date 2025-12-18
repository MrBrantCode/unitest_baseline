"""
QUESTION:
Implement the `catMouseGame` function which takes a graph as input. The graph represents a tree where each node is a position and each edge is a valid move for the cat. The cat and mouse start at positions 1 and 2 respectively. The cat and mouse move in turns, with the cat trying to catch the mouse and the mouse trying to reach the root (position 0). The function should return the outcome of the game: 0 if it's a draw, 1 if the mouse wins, and 2 if the cat wins.
"""

def catMouseGame(graph):
    n = len(graph)
    DRAW, MOUSE, CAT = 0, 1, 2
    dp = [[[DRAW for _ in range(n)] for _ in range(n)] for _ in range(2*n+1)]
    
    def parents(turn, mouse, cat):
        if turn % 2 == 0:
            for m in graph[mouse]:
                yield turn+1, m, cat
        else:
            for c in graph[cat] if cat else []:
                if c != 0:
                    yield turn+1, mouse, c
    
    def play(turn, mouse, cat):
        if turn == 2*n or mouse == cat:
            return CAT
        elif mouse == 0:
            return MOUSE
        elif dp[turn][mouse][cat] == DRAW:
            outcomes = {play(q, i, j) for q, i, j in parents(turn, mouse, cat)}
            dp[turn][mouse][cat] = (MOUSE if MOUSE in outcomes else DRAW if DRAW in outcomes else CAT)
        return dp[turn][mouse][cat]

    return play(0, 1, 2)
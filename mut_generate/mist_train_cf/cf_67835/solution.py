"""
QUESTION:
Write a function `alphabeta` that implements the Alpha-Beta pruning algorithm to evaluate the best move in a game tree. The function should take as input a `node` representing the current game state, the current `depth` of the search, and the best possible scores for the maximizing and minimizing players (`alpha` and `beta`, respectively). The function should also take a boolean `maximizingPlayer` indicating whether the current player is the maximizing player. The function should return the best possible score for the current player.
"""

def alphabeta(node, depth, alpha, beta, maximizingPlayer):
    if depth == 0 or node.isTerminal():
        return node.value
    if maximizingPlayer:
        value = float('-inf')
        for child in node.children:
            value = max(value, alphabeta(child, depth-1, alpha, beta, False))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    else:
        value = float('inf')
        for child in node.children:
            value = min(value, alphabeta(child, depth-1, alpha, beta, True))
            beta = min(beta, value)
            if beta <= alpha:
                break
        return value
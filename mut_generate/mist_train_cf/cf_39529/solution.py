"""
QUESTION:
Implement the `minimax_alpha_beta` function to determine the best move for the computer player in a tic-tac-toe game. The function should take the current game board, the active player, the current depth, alpha and beta values for pruning, a boolean indicating whether the current player is maximizing, the current move, and the original game board as input. 

It should return the optimal value, the corresponding move, and the new game board after making the move. The function should consider all possible game states and make the best move for the computer player to win or force a draw, while minimizing the opponent's chances of winning.

The game board is represented as a 3x3 list of lists, where empty spaces are denoted by ' ' (space), and each player's move is represented by their respective symbol ('X' or 'O').
"""

def minimax_alpha_beta(board, player, depth, alpha, beta, maximizing_player, move, original_board):
    # Base cases for game over or maximum depth reached
    if board.is_winner(player):
        return 1, move, board
    if board.is_winner(board.get_next_player(player)):
        return -1, move, board
    if board.is_full() or depth == 0:
        return 0, move, board

    if maximizing_player:
        max_value = float("-inf")
        best_move = None
        for possible_move in board.get_empty_spaces():
            new_board = board.get_board_copy()
            new_board.make_move(possible_move, player)
            value, _, _ = minimax_alpha_beta(new_board, player, depth - 1, alpha, beta, False, possible_move, original_board)
            if value > max_value:
                max_value = value
                best_move = possible_move
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return max_value, best_move, original_board.make_move(best_move, player)
    else:
        min_value = float("inf")
        best_move = None
        for possible_move in board.get_empty_spaces():
            new_board = board.get_board_copy()
            new_board.make_move(possible_move, board.get_next_player(player))
            value, _, _ = minimax_alpha_beta(new_board, player, depth - 1, alpha, beta, True, possible_move, original_board)
            if value < min_value:
                min_value = value
                best_move = possible_move
            beta = min(beta, value)
            if alpha >= beta:
                break
        return min_value, best_move, original_board.make_move(best_move, board.get_next_player(player))
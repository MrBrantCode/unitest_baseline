"""
QUESTION:
Implement the function `handlePawnMoves` that takes in the current game state (`game_state`), defenses (`defenses`), piece attacks (`piece_attacks`), and the en passant square (`ep_square`) as input, and returns a list of valid pawn moves based on the rules of chess. The function should handle regular pawn moves, captures, promotions, and en passant captures, and use the provided `addPawnMove` function to add valid pawn moves to the list of possible moves.
"""

def handlePawnMoves(game_state, defenses, piece_attacks, ep_square):
    moves = []
    for square, piece in game_state.board.items():
        if piece.color == game_state.current_player and piece.type == 'pawn':
            i = square.index
            value = piece_attacks[piece]
            if game_state.board[i + piece.direction] == 0:
                addPawnMove(moves, piece, i, i + piece.direction, 0, value, False)
                if piece.is_starting_position(i) and game_state.board[i + 2 * piece.direction] == 0:
                    addPawnMove(moves, piece, i, i + 2 * piece.direction, BITS_PAWN_START, value, False)
            for j in [i - 1, i + 1]:
                if game_state.board[j] != 0 and game_state.board[j].color != piece.color:
                    addPawnMove(moves, piece, i, j, 0, piece_attacks[game_state.board[j]], False)
            if square == ep_square:
                addPawnMove(moves, piece, i, ep_square, BITS_EN_PASSANT, value, False)
            if piece.is_promotion_rank(i + piece.direction):
                for promotion_type in ['queen', 'rook', 'bishop', 'knight']:
                    addPawnMove(moves, piece, i, i + piece.direction, BITS_PROMOTION, piece_attacks[promotion_type], promotion_type)
    return moves
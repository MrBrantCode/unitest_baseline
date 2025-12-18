"""
QUESTION:
Implement a function `evaluate_game` that takes a chess game as input and returns the total number of moves, captures, checks, and material balance. The game's moves, captures, and checks are determined by the 'x' and '+' characters in the move notation. The material balance is calculated by summing the piece types of the current player's pieces and subtracting the piece types of the opponent's pieces. The function should not take any additional arguments besides the chess game. The chess game is represented as a `csa` object with attributes `moves`, `turn`, and `board`.
"""

def evaluate_game(chess_game):
    total_moves = len(chess_game.moves)
    captures = sum(1 for move in chess_game.moves if 'x' in move)
    checks = sum(1 for move in chess_game.moves if '+' in move)
    
    material_balance = 0
    for piece in chess_game.board.piece_map().values():
        if piece.color == chess_game.turn:
            material_balance += piece.piece_type
        else:
            material_balance -= piece.piece_type
    
    return total_moves, captures, checks, material_balance
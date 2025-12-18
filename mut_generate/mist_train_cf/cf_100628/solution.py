"""
QUESTION:
Given a chess board represented as a nested list where each element is a tuple containing a piece and its color, write a function `find_dominant_piece` that takes this board as input and returns the position and color of the dominant piece. If there is a tie, the function should return the position and color of all tied pieces. The dominant piece is determined by the piece type, with the order of dominance being: 'K' > 'Q' > 'R' > 'B' > 'N' > 'P'.
"""

def find_dominant_piece(board):
    dominance_order = {'K': 6, 'Q': 5, 'R': 4, 'B': 3, 'N': 2, 'P': 1}
    dominant_piece = None
    dominant_color = None
    max_dominance = 0
    tied_pieces = []
    
    for i, row in enumerate(board):
        for j, square in enumerate(row):
            if square is not None:
                piece, color = square
                dominance = dominance_order[piece]
                if dominance > max_dominance:
                    dominant_piece = piece
                    dominant_color = color
                    max_dominance = dominance
                    tied_pieces = [(i, j, color)]
                elif dominance == max_dominance:
                    tied_pieces.append((i, j, color))
                    
    if len(tied_pieces) == 1:
        return tied_pieces[0]
    else:
        return tied_pieces
"""
QUESTION:
Once Volodya was at the museum and saw a regular chessboard as a museum piece. And there were only four chess pieces on it: two white rooks, a white king and a black king. "Aha, blacks certainly didn't win!", — Volodya said and was right for sure. And your task is to say whether whites had won or not.

Pieces on the chessboard are guaranteed to represent a correct position (every piece occupies one cell, no two pieces occupy the same cell and kings cannot take each other). Thus, your task is only to decide whether whites mate blacks. We would remind you that it means that the black king can be taken by one of the opponent's pieces at the moment and also it cannot move to an unbeaten position. A rook moves vertically or horizontally by any number of free cells (assuming there are no other pieces on its path), a king — to the adjacent cells (either by corner or by side). Certainly, pieces cannot leave the board. The black king might be able to take opponent's rooks at his turn (see sample 3).

Input

The input contains 4 space-separated piece positions: positions of the two rooks, the white king and the black king. Each position on 8 × 8 chessboard is denoted by two symbols — ('a' - 'h') and ('1' - '8') — which stand for horizontal and vertical coordinates of the cell occupied by the piece. It is guaranteed, that no two pieces occupy the same cell, and kings cannot take each other.

Output

Output should contain one word: "CHECKMATE" if whites mate blacks, and "OTHER" otherwise.

Examples

Input

a6 b4 c8 a8


Output

CHECKMATE


Input

a6 c4 b6 b8


Output

OTHER


Input

a2 b1 a3 a1


Output

OTHER
"""

def is_checkmate(rook1_pos, rook2_pos, white_king_pos, black_king_pos):
    def pos_to_coords(pos):
        return ord(pos[0]) - ord('a'), int(pos[1]) - 1

    def mark_rook_moves(board, x, y):
        for i in range(8):
            board[x][i] = 1
            board[i][y] = 1

    def mark_king_moves(board, x, y):
        for i in range(-1, 2):
            for j in range(-1, 2):
                if 0 <= x + i < 8 and 0 <= y + j < 8:
                    board[x + i][y + j] = 1

    board = [[0] * 8 for _ in range(8)]

    x1, y1 = pos_to_coords(rook1_pos)
    x2, y2 = pos_to_coords(rook2_pos)
    x3, y3 = pos_to_coords(white_king_pos)
    x4, y4 = pos_to_coords(black_king_pos)

    mark_rook_moves(board, x1, y1)
    mark_rook_moves(board, x2, y2)
    mark_king_moves(board, x3, y3)

    for i in range(-1, 2):
        for j in range(-1, 2):
            if 0 <= x4 + i < 8 and 0 <= y4 + j < 8:
                if board[x4 + i][y4 + j] == 0:
                    return "OTHER"

    return "CHECKMATE"
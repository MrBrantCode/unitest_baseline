"""
QUESTION:
In a game of chess, Check is a game position in which a player's King is under attack by any of the opponent's pieces.

Bob is playing with Chess pieces. He randomly arranges three pieces on 8x8 chessboard: a black's King , a white's King and any one of the white's Queen, Knight, Bishop or Rook. Positions of these pieces are known to us (positions are described following the standard chess notations) . Bob is interested in finding if black's King is under 'check' or not?

Input:
First line contains integer T - number of test cases.
Each test case contains two lines.
First line contains two strings describing the positions of black's King and white's King
Second line contains either q, k, b, or r and its position. (q = queen, k = knight, b = bishop and r = rook)

Output:
For each test case print "check"(without quotes) if black's King is under 'check' else print "-1"(without quotes)

Constraints: 
1 ≤ T ≤ 10
Each position is a two character alpha-numeric string.
All positions in a test case will be different.
First character of each position will be a lower-case alphabet in the range [a,h] and second character will be an integer in the range [1,8]

Sample tests explanation:

SAMPLE INPUT
4
e8 e1
q a4
e7 d3
b f6
h6 g4 
k h4
d8 e1
r d3

SAMPLE OUTPUT
check
check
-1
check
"""

def is_black_king_in_check(black_king_pos, white_king_pos, other_piece_type, other_piece_pos):
    def get_coords(p):
        y_map = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
        y = y_map[p[0]]
        x = int(p[1])
        return [x, y]

    def get_slope(p1, p2):
        if p1[0] == p2[0]:
            return 0
        elif p1[1] == p2[1]:
            return 0
        else:
            return (p2[1] - p1[1]) / (p2[0] - p1[0])

    bKPoint = get_coords(black_king_pos)
    wKPoint = get_coords(white_king_pos)
    oPoint = get_coords(other_piece_pos)
    m1 = get_slope(oPoint, bKPoint)
    m2 = get_slope(oPoint, wKPoint)
    okDist = ((oPoint[1] - bKPoint[1]) ** 2 + (oPoint[0] - bKPoint[0]) ** 2) ** 0.5
    wkDist = ((wKPoint[1] - bKPoint[1]) ** 2 + (wKPoint[0] - bKPoint[0]) ** 2) ** 0.5

    if other_piece_type == 'r':
        if (oPoint[0] == bKPoint[0] or oPoint[1] == bKPoint[1]) and okDist <= wkDist:
            return 'check'
    elif other_piece_type == 'b':
        if abs(m1) == 1:
            if m1 != m2:
                return 'check'
            elif okDist <= wkDist:
                return 'check'
    elif other_piece_type == 'k':
        if (abs(m1) == 2.0 or abs(m1) == 0.5) and (abs(bKPoint[0] - oPoint[0]) + abs(bKPoint[1] - oPoint[1])) == 3:
            return 'check'
    elif other_piece_type == 'q':
        if abs(m1) == 1 or m1 == 0:
            if m1 != m2:
                return 'check'
            elif okDist <= wkDist:
                return 'check'

    return '-1'
"""
QUESTION:
Given a list of white pawns on a chessboard (any number of them, meaning from 0 to 64 and with the possibility to be positioned everywhere), determine how many of them have their backs covered by another. 
Pawns attacking upwards since we have only white ones.

Please remember that a pawn attack(and defend as well) only the 2 square on the sides in front of him. https://en.wikipedia.org/wiki/Pawn_(chess)#/media/File:Pawn_(chess)_movements.gif

This is how the chess board coordinates are defined:
ABCDEFGH8♜♞♝♛♚♝♞♜7♟♟♟♟♟♟♟♟65432♙♙♙♙♙♙♙♙1♖♘♗♕♔♗♘♖
"""

def count_covered_pawns(pawns):
    pawns_set = set(pawns)
    covered_count = 0
    
    for pawn in pawns_set:
        x, y = ord(pawn[0]), ord(pawn[1])
        # Check if there is a pawn covering the current pawn
        if {chr(x - 1) + chr(y - 1), chr(x + 1) + chr(y - 1)} & pawns_set:
            covered_count += 1
    
    return covered_count
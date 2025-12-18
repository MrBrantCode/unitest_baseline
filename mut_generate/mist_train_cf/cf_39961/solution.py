"""
QUESTION:
Implement a function `max_elimination_move(marbles)` that takes a list of integers representing the current state of the Marble Solitaire board, where 1 denotes a marble and 0 denotes an empty space. The function should return a tuple `(start_index, end_index)` representing the indices of the marble to move and the position to move it to, in order to eliminate the maximum number of marbles in a single move, following the standard rules of the game: a marble can only jump over another marble to an empty space, and the marble that was jumped over is removed from the board.
"""

def max_elimination_move(marbles):
    max_elimination = 0
    move = None

    for i in range(len(marbles)):
        if marbles[i] == 1:
            for j in range(len(marbles)):
                if marbles[j] == 0:
                    distance = abs(j - i)
                    if distance > 1 and distance % 2 == 0:
                        mid_index = (i + j) // 2
                        if marbles[mid_index] == 1:
                            elimination_count = 1 # only one marble is eliminated in each jump
                            if elimination_count > max_elimination:
                                max_elimination = elimination_count
                                move = (i, j)

    return move
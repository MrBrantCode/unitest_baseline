"""
QUESTION:
Design a function `solve_karel_game` that navigates a Karel game board and collects all beepers within the minimal time possible. The function should take a `board` object as input, where the board has methods `has_beeper()`, `pick_beeper()`, `front_is_clear()`, `move()`, `turn_left()`, `position()`, and `no_more_beepers()`. The function should return the minimum number of steps required to collect all beepers. Assume that the Karel character can only move forward, turn left, and pick up beepers.
"""

def solve_karel_game(board):
    steps = 0
    visited = set()

    while True:
        if board.has_beeper():
            board.pick_beeper()
        if not board.front_is_clear():
            board.turn_left()
            if not board.front_is_clear():
                board.turn_left()
                board.turn_left()
                if not board.front_is_clear():
                    board.turn_left()
                    board.turn_left()
                    board.turn_left()

        if board.front_is_clear():
            board.move()

        steps += 1

        if board.position() in visited:
            print("Stuck in loop")
            return steps

        visited.add(board.position())

        if board.no_more_beepers():
            print("All beepers collected")
            return steps
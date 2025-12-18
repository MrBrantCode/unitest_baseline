"""
QUESTION:
Implement a function `candyCrush` that takes a 2D list `board` representing a Candy Crush game board as input, where each cell contains an integer representing a candy color. The function should repeatedly crush and drop candies until no more candies can be crushed. The function should return the final state of the board after all possible crushes have been made.

A crush occurs when three or more adjacent cells in a row or column have the same non-zero color. When a crush occurs, the crushed candies are marked with their negative color value and then dropped to the bottom of the board. The function should continue to crush and drop candies until no more crushes are possible.

The function should modify the input board in-place. The input board is a 2D list of integers, where each integer represents a candy color. The function should return the final state of the board after all possible crushes have been made.
"""

def candyCrush(board):
    def crush(arr):
        unstable = False
        R, C = len(arr), len(arr[0])
        crush_ = [[0]* C for _ in range(R)]

        for r in range(R):
            for c in range(C - 2):
                if abs(arr[r][c]) == abs(arr[r][c+1]) == abs(arr[r][c+2]) != 0:
                    crush_[r][c] = crush_[r][c+1] = crush_[r][c+2] = 1
                    unstable = True

        for c in range(C):
            for r in range(R - 2):
                if abs(arr[r][c]) == abs(arr[r+1][c]) == abs(arr[r+2][c]) != 0:
                    crush_[r][c] = crush_[r+1][c] = crush_[r+2][c] = 1
                    unstable = True

        for r in range(R):
            for c in range(C):
                if crush_[r][c] == 1:
                    arr[r][c] = -abs(arr[r][c])

        return unstable


    def drop(arr):
        R, C = len(arr), len(arr[0])
        for c in range(C):
            r2 = R - 1
            for r1 in range(R - 1, -1, -1):
                if arr[r1][c] > 0:
                    arr[r2][c] = arr[r1][c]
                    r2 -= 1
            for r in range(r2, -1, -1):
                arr[r][c] = 0

    while True:
        crushed = crush(board)
        if not crushed: return board
        drop(board)
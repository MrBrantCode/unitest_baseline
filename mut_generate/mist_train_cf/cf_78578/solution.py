"""
QUESTION:
Implement a function `slidingPuzzle(board)` that takes a 3x3 array `board` as input, where `board[i][j]` is a permutation of `[0, 1, 2, 3, 4, 5, 6, 7, 8]`, and returns the least number of moves required to solve the puzzle, or -1 if it's impossible. The puzzle is solved if the board is in the state `[[1,2,3],[4,5,6],[7,8,0]]`. A move consists of choosing the empty square (0) and a 4-directionally adjacent number and swapping them.
"""

from heapq import heappop, heappush

def entrance(board):
    moves, used, heap = {0: {(1, 3), (0, 0)}, 1: {(0, 1), (0, 0)}, 2: {(0, 2), (0, 1)}, 3: {(1, 0), (0, 0)}, 
                         4: {(1, 1), (0, 0)}, 5: {(1, 2), (0, 1)}, 6: {(2, 0), (1, 0)}, 
                         7: {(2, 1), (1, 0)}, 8: {(2, 2), (1, 1)}}, set(), [(0, id(board), board, findZero(board))]

    while heap:
        (cost, _ ,b, zero) = heappop(heap)

        if id(b) in used:
            continue

        used.add(id(b))

        if b == [[1,2,3],[4,5,6],[7,8,0]]:
            return cost
  
        for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nei = (zero[0] + d[0], zero[1] + d[1])

            if nei in moves:
                B = [row[:] for row in b]
                B[zero[0]][zero[1]], B[nei[0]][nei[1]] = B[nei[0]][nei[1]], B[zero[0]][zero[1]]
                heappush(heap, (cost + 1 + sum(abs(B[i][j]%3 - moves[B[i][j]][1][0]) + abs(B[i][j]//3 - moves[B[i][j]][1][1])  
                                for i in range(3) for j in range(3)) - abs(b[zero[0]][zero[1]]% 3 - moves[0][1][0]) 
                                - abs(b[zero[0]][zero[1]] // 3 - moves[0][1][1]), id(B), B, nei))
    return -1

def findZero(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return (i, j)   
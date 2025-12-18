"""
QUESTION:
Think about Zuma Game. You have a row of balls on the table, colored red(R), yellow(Y), blue(B), green(G), and white(W). You also have several balls in your hand.

Each time, you may choose a ball in your hand, and insert it into the row (including the leftmost place and rightmost place). Then, if there is a group of 3 or more balls in the same color touching, remove these balls. Keep doing this until no more balls can be removed.

Find the minimal balls you have to insert to remove all the balls on the table. If you cannot remove all the balls, output -1.


Examples:
Input: "WRRBBW", "RB"
Output: -1
Explanation: WRRBBW -> WRR[R]BBW -> WBBW -> WBB[B]W -> WW

Input: "WWRRBBWW", "WRBRW"
Output: 2
Explanation: WWRRBBWW -> WWRR[R]BBWW -> WWBBWW -> WWBB[B]WW -> WWWW -> empty

Input:"G", "GGGGG"
Output: 2
Explanation: G -> G[G] -> GG[G] -> empty 

Input: "RBYYBBRRB", "YRBGB"
Output: 3
Explanation: RBYYBBRRB -> RBYY[Y]BBRRB -> RBBBRRB -> RRRB -> B -> B[B] -> BB[B] -> empty 



Note:

You may assume that the initial row of balls on the table won’t have any 3 or more consecutive balls with the same color.
The number of balls on the table won't exceed 20, and the string represents these balls is called "board" in the input.
The number of balls in your hand won't exceed 5, and the string represents these balls is called "hand" in the input.
Both input strings will be non-empty and only contain characters 'R','Y','B','G','W'.
"""

import collections

def find_min_insertions(board, hand):
    def remove_consecutive(board):
        j = 0
        for i in range(len(board) + 1):
            if i < len(board) and board[i] == board[j]:
                continue
            if i - j >= 3:
                return remove_consecutive(board[0:j] + board[i:])
            else:
                j = i
        return board

    def helper(board, hmap):
        board = remove_consecutive(board)
        if len(board) == 0:
            return 0
        cnt = float('inf')
        j = 0
        for i in range(len(board) + 1):
            if i < len(board) and board[i] == board[j]:
                continue
            need = 3 - (i - j)
            if hmap[board[j]] >= need:
                hmap[board[j]] -= need
                res = helper(board[0:j] + board[i:], hmap)
                if res != float('inf'):
                    cnt = min(cnt, res + need)
                hmap[board[j]] += need
            j = i
        return cnt

    hmap = collections.defaultdict(int)
    for c in hand:
        hmap[c] += 1
    res = helper(board, hmap)
    return -1 if res == float('inf') else res
"""
QUESTION:
Snuke has two boards, each divided into a grid with N rows and N columns. For both of these boards, the square at the i-th row from the top and the j-th column from the left is called Square (i,j).

There is a lowercase English letter written in each square on the first board. The letter written in Square (i,j) is S_{i,j}. On the second board, nothing is written yet.

Snuke will write letters on the second board, as follows:

* First, choose two integers A and B ( 0 \leq A, B < N ).
* Write one letter in each square on the second board. Specifically, write the letter written in Square ( i+A, j+B ) on the first board into Square (i,j) on the second board. Here, the k-th row is also represented as the (N+k)-th row, and the k-th column is also represented as the (N+k)-th column.



After this operation, the second board is called a good board when, for every i and j ( 1 \leq i, j \leq N ), the letter in Square (i,j) and the letter in Square (j,i) are equal.

Find the number of the ways to choose integers A and B ( 0 \leq A, B < N ) such that the second board is a good board.

Constraints

* 1 \leq N \leq 300
* S_{i,j} ( 1 \leq i, j \leq N ) is a lowercase English letter.

Input

Input is given from Standard Input in the following format:


N
S_{1,1}S_{1,2}..S_{1,N}
S_{2,1}S_{2,2}..S_{2,N}
:
S_{N,1}S_{N,2}..S_{N,N}


Output

Print the number of the ways to choose integers A and B ( 0 \leq A, B < N ) such that the second board is a good board.

Examples

Input

2
ab
ca


Output

2


Input

4
aaaa
aaaa
aaaa
aaaa


Output

16


Input

5
abcde
fghij
klmno
pqrst
uvwxy


Output

0
"""

def count_good_boards(n, s):
    # Extend each row to handle the wrap-around indexing
    extended_s = [row * 2 for row in s]
    
    good_board_count = 0
    
    for b in range(n):
        is_good_board = True
        for i in range(n):
            for j in range(n):
                if extended_s[i][b + j] != extended_s[j][b + i]:
                    is_good_board = False
                    break
            if not is_good_board:
                break
        if is_good_board:
            good_board_count += 1
    
    return good_board_count * n
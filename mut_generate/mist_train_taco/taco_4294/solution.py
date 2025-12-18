"""
QUESTION:
You have N cups and 1 ball.

The cups are arranged in a row, from left to right.

You turned down all the cups, then inserted the ball into the leftmost cup.

Then, you will perform the following Q operations:

* The i-th operation: swap the positions of the A_i-th and B_i-th cups from the left. If one of these cups contains the ball, the ball will also move.



Since you are a magician, you can cast a magic described below:

* Magic: When the ball is contained in the i-th cup from the left, teleport the ball into the adjacent cup (that is, the (i-1)-th or (i+1)-th cup, if they exist).



The magic can be cast before the first operation, between two operations, or after the last operation, but you are allowed to cast it at most once during the whole process.

Find the number of cups with a possibility of containing the ball after all the operations and possibly casting the magic.

Constraints

* 2 \leq N \leq 10^5
* 1 \leq Q \leq 10^5
* 1 \leq A_i < B_i \leq N

Input

The input is given from Standard Input in the following format:


N Q
A_1 B_1
A_2 B_2
:
A_Q B_Q


Output

Print the number of cups with a possibility of eventually containing the ball.

Examples

Input

10 3
1 3
2 4
4 5


Output

4


Input

20 3
1 7
8 20
1 19


Output

5
"""

def count_possible_ball_positions(N, Q, operations):
    num = [0] * N
    num[0] = 1
    num[1] = 2
    p = 0
    
    for a, b in operations:
        a -= 1  # Convert to 0-based index
        b -= 1  # Convert to 0-based index
        num[a], num[b] = num[b], num[a]
        
        if num[a] == 1:
            p = a
        elif num[b] == 1:
            p = b
        
        if p > 0:
            num[p - 1] = 2
        if p < N - 1:
            num[p + 1] = 2
    
    return N - num.count(0)
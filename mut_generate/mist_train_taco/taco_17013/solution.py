"""
QUESTION:
Iahub likes chess very much. He even invented a new chess piece named Coder. A Coder can move (and attack) one square horizontally or vertically. More precisely, if the Coder is located at position (x, y), he can move to (or attack) positions (x + 1, y), (x–1, y), (x, y + 1) and (x, y–1).

Iahub wants to know how many Coders can be placed on an n × n chessboard, so that no Coder attacks any other Coder.


-----Input-----

The first line contains an integer n (1 ≤ n ≤ 1000).


-----Output-----

On the first line print an integer, the maximum number of Coders that can be placed on the chessboard.

On each of the next n lines print n characters, describing the configuration of the Coders. For an empty cell print an '.', and for a Coder print a 'C'.

If there are multiple correct answers, you can print any.


-----Examples-----
Input
2

Output
2
C.
.C
"""

def max_coders_on_chessboard(n):
    # Calculate the maximum number of Coders
    max_coders = (n * n + 1) // 2
    
    # Generate the configuration of the Coders
    configuration = []
    for i in range(n):
        if i % 2 == 0:
            row = ''.join('C' if j % 2 == 0 else '.' for j in range(n))
        else:
            row = ''.join('.' if j % 2 == 0 else 'C' for j in range(n))
        configuration.append(row)
    
    return max_coders, configuration
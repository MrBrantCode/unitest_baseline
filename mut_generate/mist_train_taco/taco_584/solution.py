"""
QUESTION:
We define a magic square to be an $n\times n$ matrix of distinct positive integers from $\mbox{1}$ to $n^2$ where the sum of any row, column, or diagonal of length $n$ is always equal to the same number:  the magic constant. 

You will be given a $3\times3$ matrix $\boldsymbol{\mathrm{~S~}}$ of integers in the inclusive range $[1,9]$. We can convert any digit $\boldsymbol{a}$ to any other digit $\boldsymbol{b}$ in the range $[1,9]$ at cost of $\left|a-b\right|$.  Given $\boldsymbol{\mathrm{~S~}}$, convert it into a magic square at minimal cost. Print this cost on a new line.

Note: The resulting magic square must contain distinct integers in the inclusive range $[1,9]$.

Example  

$s = [[5, 3, 4], [1, 5, 8], [6, 4, 2]]$  

The matrix looks like this: 

5 3 4
1 5 8
6 4 2

We can convert it to the following magic square:

8 3 4
1 5 9
6 7 2

This took three replacements at a cost of $|5-8|+|8-9|+|4-7|=7$.

Function Description

Complete the formingMagicSquare function in the editor below.  

formingMagicSquare has the following parameter(s):  

int s[3][3]: a $3\times3$ array of integers  

Returns  

int:  the minimal total cost of converting the input square to a magic square 

Input Format

Each of the $3$ lines contains three space-separated integers of row $s[i]$.  

Constraints

$s[i][j]\in[1,9]$

Sample Input 0
4 9 2
3 5 7
8 1 5

Sample Output 0
1

Explanation 0

If we change the bottom right value, $s[2][2]$, from $5$ to $\boldsymbol{6}$ at a cost of $|6-5|=1$, $\boldsymbol{\mathrm{~S~}}$ becomes a magic square at the minimum possible cost.

Sample Input 1
4 8 2
4 5 7
6 1 6

Sample Output 1
4

Explanation 1

Using 0-based indexing, if we make 

$s[0][1]$->$\mbox{9}$ at a cost of $|9-8|=1$ 
$s[\mathbf{1}][\mathbf{0}]$->$3$ at a cost of $|3-4|=1$
$s[2][0]$->$8$ at a cost of $|8-6|=2$,  

then the total cost will be $1+1+2=4$.
"""

from itertools import permutations

def forming_magic_square(s):
    # Flatten the input 3x3 matrix into a 1D list
    X = [s[i][j] for i in range(3) for j in range(3)]
    
    # Initialize the minimum cost to a large number
    min_cost = 81
    
    # Iterate over all permutations of the numbers 1 to 9
    for P in permutations(range(1, 10)):
        # Check if the permutation forms a magic square
        if (sum(P[0:3]) == 15 and sum(P[3:6]) == 15 and 
            sum(P[0::3]) == 15 and sum(P[1::3]) == 15 and 
            P[0] + P[4] + P[8] == 15 and P[2] + P[4] + P[6] == 15):
            # Calculate the cost to convert the input square to this permutation
            cost = sum(abs(P[i] - X[i]) for i in range(9))
            # Update the minimum cost if this cost is lower
            min_cost = min(min_cost, cost)
    
    # Return the minimum cost found
    return min_cost
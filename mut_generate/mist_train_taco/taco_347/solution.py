"""
QUESTION:
Two players called $\mathbf{P1}$ and $\textbf{P2}$ are playing a game with a starting number of stones. Player $1$ always plays first, and the two players move in alternating turns. The game's rules are as follows:

In a single move, a player can remove either $2$, $3$, or $5$ stones from the game board. 
If a player is unable to make a move, that player loses the game.

Given the starting number of stones, find and print the name of the winner.  $\mathbf{P1}$ is named First and $\textbf{P2}$ is named Second.  Each player plays optimally, meaning they will not make a move that causes them to lose the game if a winning move exists.

For example, if $n=4$, $\mathbf{P1}$ can make the following moves:  

$\mathbf{P1}$ removes $2$ stones leaving $2$. $\textbf{P2}$ will then remove $2$ stones and win.
$\mathbf{P1}$ removes $3$ stones leaving $1$. $\textbf{P2}$ cannot move and loses.

$\mathbf{P1}$ would make the second play and win the game.

Function Description

Complete the gameOfStones function in the editor below.  It should return a string, either First or Second.  

gameOfStones has the following parameter(s):

n: an integer that represents the starting number of stones

Input Format

The first line contains an integer $\boldsymbol{\boldsymbol{t}}$, the number of test cases. 

Each of the next $\boldsymbol{\boldsymbol{t}}$ lines contains an integer $n$, the number of stones in a test case.

Constraints

$1\le n,t\le100$

Output Format

On a new line for each test case, print First if the first player is the winner.  Otherwise print Second.

Sample Input
8
1
2
3
4
5
6
7
10

Sample Output
Second
First
First
First
First
First
Second
First

Explanation

In the sample, we have $t=8$ testcases.  

If $n=1$, $\mathbf{P1}$ can't make any moves and loses the game.

If $n=2$, $\mathbf{P1}$ removes $2$ stones and wins the game.

If $n=3$, $\mathbf{P1}$ removes $2$ stones in their first move, leaving $1$ stone on the board and winning the game.  

If $n=4$, $\mathbf{P1}$ removes $3$ stones in their first move, leaving $1$ stone on the board and winning the game.  

If $n=5$, $\mathbf{P1}$ removes all $5$ stones from the game board, winning the game.  

If $n=6$, $\mathbf{P1}$ removes $5$ stones in their first move, leaving $1$ stone on the board and winning the game.  

If $n=7$, $\mathbf{P1}$ can make any of the following three moves:

Remove $2$ stones, leaving $5$ stones on the board. $\textbf{P2}$ then removes $5$ stones, winning the game.  
Remove $3$ stones, leaving $4$ stones on the board. $\textbf{P2}$ then removes $3$ stones, leaving $1$ stone left on the board and winning the game.  
Remove $5$ stones, leaving $2$ stones on the board. $\textbf{P2}$ then removes the $2$ remaining stones and wins the game.  

All possible moves result in $\textbf{P2}$ winning.

If $n=10$, $\mathbf{P1}$ can remove either $2$ or $3$ stones to win the game.
"""

def determine_winner(n: int) -> str:
    # Precomputed lists based on the game rules
    First = [2, 3, 4, 5, 6, 9, 10]
    Second = [1, 7, 8]
    
    # Extend the lists up to 100 based on the game rules
    for i in range(11, 101):
        if i - 2 in Second or i - 3 in Second or i - 5 in Second:
            First.append(i)
        else:
            Second.append(i)
    
    # Determine the winner based on the precomputed lists
    if n in First:
        return 'First'
    else:
        return 'Second'
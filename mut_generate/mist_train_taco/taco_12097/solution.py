"""
QUESTION:
Kyle and Mike are bored on a rainy day and decide to pass the time by creating a new game having the following rules:

The game starts with two $n$-sized integer arrays, $\mbox{A}$ and $\mbox{B}$, and is played by two players, $\mathbf{P_1}$ and $P_2$. 
The players move in alternating turns, with $\mathbf{P_1}$ always moving first. During each move, the current player must choose an integer, $\boldsymbol{i}$, such that $0\leq i\leq n-1$. If the current player is $\mathbf{P_1}$, then $\mathbf{P_1}$ receives $A_i$ points; if the current player is $P_2$, then $P_2$ receives $B_i$ points.
Each value of $\boldsymbol{i}$ can be chosen only once. That is, if a value of $\boldsymbol{i}$ is already chosen by some player, none of the player can re-use it. So, game always ends after $n$ moves.
The player with the maximum number of points wins.
The arrays A and B are accessible to both the players P1 and P2. So the players make a optimal move at every turn. 

Given the values of $n$, $\mbox{A}$, and $\mbox{B}$, can you determine the outcome of the game? Print $\textbf{First}$ if $\mathbf{P_1}$ will win, $\textbf{Second}$ if $P_2$ will win, or $\textbf{Tie}$ if they will tie. Assume both players always move optimally.

Input Format

The first line of input contains a single integer, $\mathbf{T}$, denoting the number of test cases. Each of the $3T$ subsequent lines describes a test case. A single test case is defined over the following three lines:

An integer, $n$, denoting the number of elements in arrays $\mbox{A}$ and $\mbox{B}$.
$n$ space-separated integers, $A_0,A_1,\ldots,A_{n-1}$, where each $A_i$ describes the element at index $\boldsymbol{i}$ of array $\mbox{A}$.
$n$ space-separated integers, $B_{0},B_{1},...,B_{n-1}$, where each $B_i$ describes the element at index $\boldsymbol{i}$ of array $\mbox{B}$.

Constraints

$1\leq T\leq10$ 
$1\leq n\leq1000$ 
$1\leq A_i,B_i\leq10^5$ 

Output Format

For each test case, print one of the following predicted outcomes of the game on a new line:

Print $\textbf{First}$ if $\mathbf{P_1}$ will win.
Print $\textbf{Second}$ if $P_2$ will win.
Print $\textbf{Tie}$ if the two players will tie.

Sample Input
3
3
1 3 4
5 3 1
2
1 1
1 1
2
2 2
3 3

Sample Output
First
Tie
Second

Explanation

Test Case 0: $A=\{1,3,4\}$, $B=\{5,3,1\}$
The players make the following $n$ moves:

$\mathbf{P_1}$ chooses $i=2$ and receives $4$ points.
$P_2$ chooses $i=\textbf{0}$ and receives $5$ points. Note that $P_2$ will not choose $i=1$, because this would cause $\mathbf{P_1}$ to win.
$\mathbf{P_1}$ chooses $i=1$ (which is the only remaining move) and receives $3$ points.

As all $n=3$ moves have been made, the game ends. $\mathbf{P_1}$'s score is $7$ points and $P_2$'s score is $5$ points, so $\mathbf{P_1}$ is the winner and we print $\textbf{First}$ on a new line.

Test Case 1: $A=\{1,1\}$, $B=\{1,1\}$
Because both players will only make $1$ move and all possible point values are $1$, the players will end the game with equal scores. Thus, we print $\textbf{Tie}$ on a new line.

Test Case 1: $A=\{2,2\}$, $B=\{3,3\}$ 

Because both players will only make $1$ move and all the possible point values for $P_2$ are greater than all the possible point values for $\mathbf{P_1}$, $P_2$ will win the game. Thus, we print $\textbf{Second}$ on a new line.
"""

def determine_game_outcome(n, A, B):
    # Calculate the combined scores for each index
    combined_scores = [A[i] + B[i] for i in range(n)]
    
    # Initialize scores for both players
    P1_score = 0
    P2_score = 0
    
    # Determine the optimal moves for both players
    for _ in range(n):
        # Find the index with the maximum combined score
        max_index = combined_scores.index(max(combined_scores))
        
        # Player P1 moves first
        if _ % 2 == 0:
            P1_score += A[max_index]
        else:
            P2_score += B[max_index]
        
        # Remove the chosen index from all lists
        combined_scores.pop(max_index)
        A.pop(max_index)
        B.pop(max_index)
    
    # Determine the outcome of the game
    if P1_score > P2_score:
        return "First"
    elif P2_score > P1_score:
        return "Second"
    else:
        return "Tie"
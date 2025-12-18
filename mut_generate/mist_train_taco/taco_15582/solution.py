"""
QUESTION:
We have a deck consisting of N cards. Each card has an integer written on it. The integer on the i-th card from the top is a_i.

Two people X and Y will play a game using this deck. Initially, X has a card with Z written on it in his hand, and Y has a card with W written on it in his hand. Then, starting from X, they will alternately perform the following action:

* Draw some number of cards from the top of the deck. Then, discard the card in his hand and keep the last drawn card instead. Here, at least one card must be drawn.



The game ends when there is no more card in the deck. The score of the game is the absolute difference of the integers written on the cards in the two players' hand.

X will play the game so that the score will be maximized, and Y will play the game so that the score will be minimized. What will be the score of the game?

Constraints

* All input values are integers.
* 1 \leq N \leq 2000
* 1 \leq Z, W, a_i \leq 10^9

Input

Input is given from Standard Input in the following format:


N Z W
a_1 a_2 ... a_N


Output

Print the score.

Examples

Input

3 100 100
10 1000 100


Output

900


Input

3 100 1000
10 100 100


Output

900


Input

5 1 1
1 1 1 1 1


Output

0


Input

1 1 1
1000000000


Output

999999999
"""

def calculate_game_score(N, Z, W, a):
    if N == 1:
        return abs(a[0] - W)
    
    x = [-1] * N
    y = [-1] * N
    
    x[N - 1] = abs(a[N - 1] - W)
    y[N - 2] = abs(a[N - 1] - a[N - 2])
    
    for i in range(N - 2, -1, -1):
        x[i] = abs(a[i] - a[N - 1])
        for j in range(i + 1, N - 1):
            x[i] = min(x[i], y[j])
        
        y[i] = abs(a[N - 1] - a[i])
        for j in range(i + 1, N - 1):
            y[i] = max(y[i], x[j])
    
    return max(x)
"""
QUESTION:
Alice and Bob take turns playing a game, with Alice starting first.
Initially, there is a number N on the chalkboard.  On each player's turn, that player makes a move consisting of:

Choosing any x with 0 < x < N and N % x == 0.
Replacing the number N on the chalkboard with N - x.

Also, if a player cannot make a move, they lose the game.
Return True if and only if Alice wins the game, assuming both players play optimally.
 



Example 1:
Input: 2
Output: true
Explanation: Alice chooses 1, and Bob has no more moves.


Example 2:
Input: 3
Output: false
Explanation: Alice chooses 1, Bob chooses 1, and Alice has no more moves.

 
Note:

1 <= N <= 1000
"""

def alice_wins_game(N: int) -> bool:
    """
    Determines if Alice wins the game given the initial number N on the chalkboard.
    
    Alice and Bob take turns playing a game, with Alice starting first. On each player's turn, 
    that player makes a move by choosing any x with 0 < x < N and N % x == 0, and then replacing 
    the number N on the chalkboard with N - x. If a player cannot make a move, they lose the game.
    
    Args:
        N (int): The initial number on the chalkboard.
        
    Returns:
        bool: True if Alice wins the game, False otherwise.
    """
    return N % 2 == 0
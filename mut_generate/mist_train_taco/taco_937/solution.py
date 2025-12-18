"""
QUESTION:
We define a function f on a binary string S of length N as follows:

f(S) = \sum_{i = 1}^{N - 1} |S_{i+1} - S_{i}|.

JJ and Uttu have a binary string S of length N and they decide to play a game using it. The rules of the game are as follows:

JJ starts the game with players making moves in alternate turns thereafter.
In one move, a player can pick L, R such that 1 ≤ L ≤ R ≤ N and flip all the characters in S_{L \dots R} (Flipping a character means changing 0 to 1 or 1 to 0).
A player can only make a move if that move increases the value of f(S).
The player who can not make any further moves loses.

Which player (out of JJ and Uttu) will win the game, assuming that both the players play optimally?

------ Input Format ------ 

- The first line contains T - the number of test cases. Then the test cases follow.
- The first line of each test case contains N -  the length of the binary string S.
- The second line of each test case contains a binary string S.

------ Output Format ------ 

For each test case, output which player wins the game, whether it's JJ and Uttu will win the game.

You may print each character of the string in uppercase or lowercase (for example, the strings JJ, Jj and jj will all be treated as identical).

------ Constraints ------ 

$1 ≤ T ≤ 100$
$1 ≤ N ≤ 2000$

----- Sample Input 1 ------ 
3
5
10011
2
00
5
10101
----- Sample Output 1 ------ 
JJ
JJ
Uttu
----- explanation 1 ------ 
- Test case $1$: JJ can perform the following move: $10\underline{01}1 \rightarrow 10101$. Now Uttu cannot perform any moves and thereby loses.
- Test case $2$: JJ can perform the following move: $0\underline{0} \rightarrow 01$. Now Uttu cannot perform any moves and thereby loses.
- Test case $3$: JJ cannot perform any starting moves, thereby he loses.
"""

def determine_winner(N: int, S: str) -> str:
    """
    Determines the winner of the game between JJ and Uttu given a binary string S of length N.
    
    Parameters:
    - N (int): The length of the binary string S.
    - S (str): The binary string.
    
    Returns:
    - str: The winner of the game ('JJ' or 'Uttu').
    """
    from functools import lru_cache
    
    @lru_cache(None)
    def fn(cnt):
        if cnt == 0:
            return False
        ans = False
        if cnt >= 1:
            if fn(cnt - 1) == False:
                ans = True
        if not ans and cnt >= 2:
            if fn(cnt - 2) == False:
                ans = True
        return ans
    
    cnt = sum((int(ch1 == ch2) for (ch1, ch2) in zip(S, S[1:])))
    if fn(cnt):
        return 'JJ'
    else:
        return 'Uttu'
"""
QUESTION:
Bob sees his younger brother, Jack, playing Stepping Stones. He is fascinated by the most interesting game and decides to play it.

Square boxes have been made on the ground with the help of chalk powder, and a number is assigned to each block. Bob is standing in front of these  blocks. From here, he will throw a stone 1 block far, move to that block; pick up the stone and then he will throw the stone two blocks far from here, move to that block; pick up the stone, and throw the stone three blocks far from here, move to that block, and so on. What's the catch of the game??. The catch of the game is to check if it is possible to reach $N^{\mbox{th}}$ block in this manner.  

Bob is a bit lazy. He will make a move only if he is sure that he can reach the $N^{\mbox{th}}$ block. So, tell him if he should make a move or not?  

Input Format 

First line of input contains an integer $\mathbf{T}$ denoting the number of times Bob plays this game. Each of the next $\mathbf{T}$ lines contains a single integer $N$ denoting the $N^{\mbox{th}}$ block.  

Output Format 

Output consists of several lines as per the following criteria: If bob is able to reach $N^{\mbox{th}}$ block, then print Go On Bob with the number of moves required to reach to the $N^{\mbox{th}}$ block both separated by a space. If Bob is not able to reach the $N^{\mbox{th}}$ block, then print Better Luck Next Time.

Constraints

$1\leq T\leq10^5$ 

$1\leq N\leq10^{18}$

Sample Input #00:

1
2

Sample Output #00:

Better Luck Next Time

Explanation: #00:

Bob can jump to the $1^{st}$ Block. From here, he is allowed to make a move to the $3^{rd}$ Block only. So,he cannot step onto $2^{nd}$ Block.  

Sample Input #01:  

1
3

Sample Output #01:

Go On Bob 2

Explanation: #01:

As explained in the previous test case, Bob can make a second move to reach to the $3^{rd}$ Block. So, he can step on $3^{rd}$ block in just 2 moves.
"""

from math import sqrt

def can_reach_block(N):
    j = (1 + sqrt(1 + 8 * N)) / 2
    if abs(j - int(j)) <= 0:
        return ("Go On Bob", int(j - 1))
    else:
        return ("Better Luck Next Time", None)
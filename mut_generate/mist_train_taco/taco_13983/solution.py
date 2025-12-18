"""
QUESTION:
Do you remember the game of Snakes and Ladders ? We have removed all the snakes from the board. However to compensate for the loss of trouble, we have enlarged the board from a maximum limit (Target Square) of 100 to a maximum limit (Target Square) of N ≥ 100, N being a perfect square.

Rani has a match with Nandu on this new kind of board next week. 

Now Rani is practising alone on the board. Suddenly Rani starts wondering : "Suppose I have total control over both my dice (each die being a standard 1-6 die) and I am the only player playing all the turns such that in each turn I throw both the dice, what is the minimum number of turns in which I can reach the Target Square N ? " 

Given the configuration of the board ie. given all the information about the location of Ladders on the board, find the answer to Rani's question. 

Note (to player) : 
You start from Square Number 1.
If you reach a square which contains the base of a ladder, you have to climb up that ladder in the same turn itself (it is compulsory to climb the ladder). Note that you can only climb up ladders, not climb down. 
Say you are at square number N-2. The only way you can complete the
   game is by getting a 2 by throwing both your dice. If you throw a 4
   or a 5 or anything else, your turn goes wasted.

Input :

First line consisits of T denoting the number of test cases. The first line of each test case consists of 2 space-separated integers N an L denoting the Target Square and number of ladders respectively. The next L lines are such that each line consists of 2-space separated integers B and U denoting the squares  where the bottom and upper parts of each ladder lie.

Ouptut:

Print a single integer per test case on a new line, the answer to Rani's question.

Constraints :

1 ≤ T ≤ 3

100 ≤ N ≤ 160000, N being a perfect square

0 ≤ L ≤ SquareRoot(N)

1 ≤ B<U ≤ N

Author : Shreyans

Tester : Sandeep

(By IIT Kgp HackerEarth Programming Club)

SAMPLE INPUT
1
100 1
5 97

SAMPLE OUTPUT
2

Explanation

In the first turn, Rani will drop 4 using both her dice. So, 1 -> 5. Now there is a ladder going from 5 to 97. 
So, now Rani's piece will climb the ladder and reach 97. 

In her second turn, Rani will drop a 3 using both her dice. So, 97 -> 100. 
Hence Rani reaches the Target Square in 2 turns.
"""

def minimum_turns_to_reach_target(N, ladders):
    # Initialize the board with a large value (infinity)
    a = [100000] * (N + 20)
    # Initialize the ladder positions
    s = [0] * (N + 20)
    
    # Set up the ladders
    for (B, U) in ladders:
        s[B] = U
    
    # Starting position
    a[1] = 0
    
    # If there's a ladder at the starting position, update the board
    if s[1] != 0:
        z = s[1]
        while z != 0:
            a[z] = 0
            z = s[z]
    
    # Dynamic programming to find the minimum turns
    for i in range(1, N):
        if s[i] == 0 and a[i] != 100000:
            for j in range(2, 13):
                if i + j <= N and a[i + j] > a[i] + 1:
                    a[i + j] = a[i] + 1
                    z = s[i + j]
                    while z != 0 and i + j <= N:
                        a[z] = a[i + j]
                        z = s[z]
    
    # Return the minimum number of turns to reach the target square N
    return a[N]
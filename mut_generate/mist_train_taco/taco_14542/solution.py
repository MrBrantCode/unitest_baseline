"""
QUESTION:
Tug of war is a sport that directly puts two teams against each other in a test of strength.

During school days, both Chef Shifu and Chef Po were champions of tug of war.
On behalf of restaurant's anniversary, Chef Shifu and Chef Po have decided to conduct 
a tug of war game for their customers.

Master Chef Oogway has decided the following rules for the game.

Let N be the number of players participating in the game. All of these 
players would stand in a circle in clock wise direction.
    
There are an infinite number of long ropes available.
When a rope is held by exactly two players, it is termed as bonding.
    
At least one bonding is necessary to conduct a game.
    
A player can play against multiple people simultaneously i.e he can have more than one bonding at
the same time. 
    
Both members of a pair of players that have a bonding must have the same number of total
bondings. That is, if the player A  makes bonding with the player B,
then the number of total bondings of the player A must be the same as
that of the player B.
    
Bondings should be created in such a fashion that ropes must not intersect each other. 
    
The number of bondings of every player must be no more than K.
    
Now Master Chef Oogway asked Chef Shifu and Chef Po to find out the number of possible games.
Your task is to help them find this number. As this number might become huge,
you've to find it modulo (10^{14}+7). Two games are different iff there is some
bonding that is present in only of them. 

------ Input ------ 

First line contains T, the number of test cases.
Each of T lines contain 2 positive integers N and K separated by a space.

------ Output ------ 

For each test case, output the number of ways to conduct the game modulo 100000000000007 (10^{14}+7) in one line.

------ Example ------ 

Input:
3
3 2
4 0
2 1

Output:
4
0
1

Explanation:

For the 1st case, there are 3 players. Let's call them p1, p2, p3.
Different games possible are:

Game 1: p1-p2 (numbers of bondings of p1, p2 are 1 ≤ K = 2)

Game 2: p1-p3 (numbers of bondings of p1, p3 are 1 ≤ K = 2)

Game 3: p2-p3 (numbers of bondings of p2, p3 are 1 ≤ K = 2)

Game 4: p1-p2, p1-p3, p2-p3 (numbers of bondings of p1, p2, p3 are 2 ≤ K
= 2)

For the 2nd test case, we cannot form the game, because K = 0 and hence no
player is allowed to make any bonding. As any game must have atleast one
bonding, no game is possible here. 

For the 3rd case, only possible game is:

Game 1: p1-p2 (number of bondings in p1, p2 are 1)

------ Constraints ------ 

1 ≤ T ≤ 10000
0 ≤ N ≤ 10000
0 ≤ K ≤ N
"""

def calculate_possible_games(N: int, K: int) -> int:
    """
    Calculate the number of possible games of tug of war with N players and at most K bondings per player.

    Parameters:
    N (int): The number of players.
    K (int): The maximum number of bondings per player.

    Returns:
    int: The number of possible games modulo 100000000000007.
    """
    mod = 100000000000007
    
    # Precompute Motzkin and Catalan numbers
    motzkin = [1, 0]
    catalan = [1, 1, 2]
    
    for i in range(1, 10009):
        motzkin.append(0)
    for j in range(0, 10006):
        catalan.append(0)
    
    for i in range(2, 10006):
        motzkin[i] = (i - 1) * (2 * motzkin[i - 1] + 3 * motzkin[i - 2])
        motzkin[i] = motzkin[i] // (i + 1)
    
    for i in range(10003):
        motzkin[i] = (motzkin[i] + motzkin[i + 1]) % mod
    
    for i in range(2, 10001):
        catalan[i + 1] = (4 * i + 2) * catalan[i] // (i + 2)
    
    # Calculate the result based on the values of N and K
    if K == 0:
        return 0
    elif K == 1:
        return (motzkin[N] - 1) % mod
    else:
        return (catalan[N] - 1) % mod
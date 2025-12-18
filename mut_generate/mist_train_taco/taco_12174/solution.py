"""
QUESTION:
Team India is playing too much cricket in this season. Team players are getting better in their performance with match by match. Sir Jadeja has become a Trump Card for M.S Dhoni. There is a hidden reason of his special position in the team. He can make new copies of a person by some magic. Due to this, players can get many chances to bat. Now there is a fixed batting line up of top 7 batsman decided by Dhoni as : [ "Rohit", "Dhawan", "Kohli", "Yuvraj", "Raina" , "Dhoni", "Sir Jadeja"]. Now they are playing one ball at a time and once they play a ball, Jadeja will make a new copy of that player (including himself) and both the same players will get back in this batting line up. In this way they will get a chance to play a ball turn by turn. Your task is very simple. You are required to output the name of a player as given in the above list who will play a K^th ball.

Input

First line will contain T (No. of test cases).
Each test case will consist of one line containing the value of K .

Output

For every test case, print a new line having the name of a player who will play the K^th ball. 

Constraints

1 ≤ T ≤ 1000
1 ≤ K ≤ 10^9

SAMPLE INPUT
2
3
9

SAMPLE OUTPUT
Kohli
Rohit

Explanation

In second test case where K = 9, Sequence after the 7th ball will become Rohit, Rohit, Dhawan, Dhawan, Kohli, Kohli, Yuvraj, Yuvraj, Raina, Raina, Dhoni, Dhoni, Sir Jadeja, Sir Jadeja. So 8th and 9th ball will be played by Rohit.
"""

import math

def find_batsman_for_kth_ball(k: int, batting_lineup: list) -> str:
    # Calculate the number of times the lineup has been doubled
    val = math.log(k / len(batting_lineup) + 1) / math.log(2)
    n = int(math.ceil(val))
    
    # Calculate the sum of the geometric series up to the (n-1)th term
    sn_1 = len(batting_lineup) * (int(math.pow(2, n - 1)) - 1)
    
    # Calculate the index in the current lineup
    inte = math.ceil(((k - sn_1) / math.pow(2, n - 1)))
    
    # Return the player name at the calculated index
    return batting_lineup[int(inte) - 1]
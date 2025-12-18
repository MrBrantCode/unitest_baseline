"""
QUESTION:
You are a cricket coach who wants to partition a set of players into two teams of equal size and a referee. If there are odd players, one of the player becomes the referee. However, if there are even players, the coach himself acts as the referee. Each player has a score (integer) associated with him, known only to the coach. More than one player can have the same score. [If there are zero players, the coach is the referee]                                                                            

The most fair partitioning for the set is given when F(s1, s2) is minimized, where s1 and s2 are the sets representing the teams.                               

F(s1, s2) = abs(g(s1) - g(s2))                                                     

g(s) = sum of scores of players in s                                                   

He is in an evil mood today and wants to create the most unfair partitioning. Another issue
is that players keep coming in for the game and he wants to create teams as and when they come.

This is too hard for him and he has asked you to help him out. He has asked you 
to create a computer program that can take in scores ( > 0) of players as input and when the input score is 0, return the score of the referee such the most unfair partitioning is obtained. If he should act as the referee, your program should output -1. Your program should stop when the input received is -2.          

INPUT FORMAT                                                                       

A single number, N ( ≤ 1000000000) on every line is given as input with the last input being -2. There will be at most 100000 lines.

OUTPUT FORMAT                                                                      

Every time your program encounters a '0', you should return the score of the player
that acts as referee.

SAMPLE INPUT
4
1
3
0
1
0
-2

SAMPLE OUTPUT
3
-1
"""

from heapq import heappush, heappop

def partition_teams(scores):
    minH = []
    maxH = []
    referee_scores = []
    
    for score in scores:
        if score == -2:
            break
        
        if score == 0:
            if len(minH) == len(maxH):
                referee_scores.append(-1)
            else:
                if len(minH) > len(maxH):
                    referee_scores.append(minH[0])
                else:
                    referee_scores.append(-maxH[0])
        else:
            if len(minH) == 0 and len(maxH) == 0:
                heappush(minH, score)
            else:
                if score < minH[0]:
                    heappush(maxH, -score)
                else:
                    heappush(minH, score)
                    heappush(maxH, -heappop(minH))
                
                if (len(maxH) - len(minH)) >= 2:
                    heappush(minH, -heappop(maxH))
    
    return referee_scores
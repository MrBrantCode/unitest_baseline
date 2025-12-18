"""
QUESTION:
Petya loves football very much, especially when his parents aren't home. Each morning he comes to the yard, gathers his friends and they play all day. From time to time they have a break to have some food or do some chores (for example, water the flowers).

The key in football is to divide into teams fairly before the game begins. There are n boys playing football in the yard (including Petya), each boy's football playing skill is expressed with a non-negative characteristic ai (the larger it is, the better the boy plays). 

Let's denote the number of players in the first team as x, the number of players in the second team as y, the individual numbers of boys who play for the first team as pi and the individual numbers of boys who play for the second team as qi. Division n boys into two teams is considered fair if three conditions are fulfilled:

  * Each boy plays for exactly one team (x + y = n). 
  * The sizes of teams differ in no more than one (|x - y| ≤ 1). 
  * The total football playing skills for two teams differ in no more than by the value of skill the best player in the yard has. More formally: <image>



Your task is to help guys divide into two teams fairly. It is guaranteed that a fair division into two teams always exists.

Input

The first line contains the only integer n (2 ≤ n ≤ 105) which represents the number of guys in the yard. The next line contains n positive space-separated integers, ai (1 ≤ ai ≤ 104), the i-th number represents the i-th boy's playing skills. 

Output

On the first line print an integer x — the number of boys playing for the first team. On the second line print x integers — the individual numbers of boys playing for the first team. On the third line print an integer y — the number of boys playing for the second team, on the fourth line print y integers — the individual numbers of boys playing for the second team. Don't forget that you should fulfil all three conditions: x + y = n, |x - y| ≤ 1, and the condition that limits the total skills.

If there are multiple ways to solve the problem, print any of them.

The boys are numbered starting from one in the order in which their skills are given in the input data. You are allowed to print individual numbers of boys who belong to the same team in any order.

Examples

Input

3
1 2 1


Output

2
1 2 
1
3 


Input

5
2 3 3 1 1


Output

3
4 1 3 
2
5 2 

Note

Let's consider the first sample test. There we send the first and the second boy to the first team and the third boy to the second team. Let's check all three conditions of a fair division. The first limitation is fulfilled (all boys play), the second limitation on the sizes of groups (|2 - 1| = 1 ≤ 1) is fulfilled, the third limitation on the difference in skills ((2 + 1) - (1) = 2 ≤ 2) is fulfilled.
"""

def divide_into_teams(n, skills):
    # Create a list of tuples where each tuple contains the skill and the original index (1-based)
    pos = [(skills[i], i + 1) for i in range(n)]
    
    # Sort the list based on skills
    pos.sort()
    
    # Initialize teams
    team1 = []
    team2 = []
    
    # Distribute boys into teams alternately
    for i in range(n):
        if i % 2 == 0:
            team1.append(pos[i][1])
        else:
            team2.append(pos[i][1])
    
    # Return the results
    return len(team1), team1, len(team2), team2
"""
QUESTION:
Any resemblance to any real championship and sport is accidental.

The Berland National team takes part in the local Football championship which now has a group stage. Let's describe the formal rules of the local championship: 

  * the team that kicked most balls in the enemy's goal area wins the game; 
  * the victory gives 3 point to the team, the draw gives 1 point and the defeat gives 0 points; 
  * a group consists of four teams, the teams are ranked by the results of six games: each team plays exactly once with each other team; 
  * the teams that get places 1 and 2 in the group stage results, go to the next stage of the championship. 



In the group stage the team's place is defined by the total number of scored points: the more points, the higher the place is. If two or more teams have the same number of points, then the following criteria are used (the criteria are listed in the order of falling priority, starting from the most important one): 

  * the difference between the total number of scored goals and the total number of missed goals in the championship: the team with a higher value gets a higher place; 
  * the total number of scored goals in the championship: the team with a higher value gets a higher place; 
  * the lexicographical order of the name of the teams' countries: the country with the lexicographically smaller name gets a higher place. 



The Berland team plays in the group where the results of 5 out of 6 games are already known. To be exact, there is the last game left. There the Berand national team plays with some other team. The coach asks you to find such score X:Y (where X is the number of goals Berland scored and Y is the number of goals the opponent scored in the game), that fulfills the following conditions: 

  * X > Y, that is, Berland is going to win this game; 
  * after the game Berland gets the 1st or the 2nd place in the group; 
  * if there are multiple variants, you should choose such score X:Y, where value X - Y is minimum; 
  * if it is still impossible to come up with one score, you should choose the score where value Y (the number of goals Berland misses) is minimum. 

Input

The input has five lines.

Each line describes a game as "team1 team2 goals1:goals2" (without the quotes), what means that team team1 played a game with team team2, besides, team1 scored goals1 goals and team2 scored goals2 goals. The names of teams team1 and team2 are non-empty strings, consisting of uppercase English letters, with length of no more than 20 characters; goals1, goals2 are integers from 0 to 9. 

The Berland team is called "BERLAND". It is guaranteed that the Berland team and one more team played exactly 2 games and the the other teams played exactly 3 games.

Output

Print the required score in the last game as X:Y, where X is the number of goals Berland scored and Y is the number of goals the opponent scored. If the Berland team does not get the first or the second place in the group, whatever this game's score is, then print on a single line "IMPOSSIBLE" (without the quotes).

Note, that the result score can be very huge, 10:0 for example.

Examples

Input

AERLAND DERLAND 2:1
DERLAND CERLAND 0:3
CERLAND AERLAND 0:1
AERLAND BERLAND 2:0
DERLAND BERLAND 4:0


Output

6:0


Input

AERLAND DERLAND 2:2
DERLAND CERLAND 2:3
CERLAND AERLAND 1:3
AERLAND BERLAND 2:1
DERLAND BERLAND 4:1


Output

IMPOSSIBLE

Note

In the first sample "BERLAND" plays the last game with team "CERLAND". If Berland wins with score 6:0, the results' table looks like that in the end: 

  1. AERLAND (points: 9, the difference between scored and missed goals: 4, scored goals: 5) 
  2. BERLAND (points: 3, the difference between scored and missed goals: 0, scored goals: 6) 
  3. DERLAND (points: 3, the difference between scored and missed goals: 0, scored goals: 5) 
  4. CERLAND (points: 3, the difference between scored and missed goals: -4, scored goals: 3) 



In the second sample teams "AERLAND" and "DERLAND" have already won 7 and 4 points, respectively. The Berland team wins only 3 points, which is not enough to advance to the next championship stage.
"""

import copy

def calculate_berland_score(games):
    teams = {}
    times = {}

    def put_team(s):
        if s[0] not in teams:
            teams[s[0]] = [0, 0, 0, s[0]]
        if s[1] not in teams:
            teams[s[1]] = [0, 0, 0, s[1]]
        (g1, g2) = map(int, s[2].split(':'))
        teams[s[0]][1] -= g1 - g2
        teams[s[1]][1] -= g2 - g1
        teams[s[0]][2] -= g1
        teams[s[1]][2] -= g2
        if g1 > g2:
            teams[s[0]][0] -= 3
        elif g1 < g2:
            teams[s[1]][0] -= 3
        else:
            teams[s[0]][0] -= 1
            teams[s[1]][0] -= 1

    def add_times(s):
        times[s[0]] = times.get(s[0], 0) + 1
        times[s[1]] = times.get(s[1], 0) + 1

    for game in games:
        s = game.split()
        put_team(s)
        add_times(s)

    t1, t2 = 'BERLAND', ''
    for k, v in times.items():
        if v == 2 and k != t1:
            t2 = k

    cpy_teams = copy.deepcopy(teams)
    res = (2000000000.0, 0, 'IMPOSSIBLE')

    for g1 in range(60):
        for g2 in range(60):
            if g1 > g2:
                teams = copy.deepcopy(cpy_teams)
                put_team(('%s %s %d:%d' % (t1, t2, g1, g2)).split())
                s = sorted(teams.values())
                if t1 == s[0][3] or t1 == s[1][3]:
                    res = min(res, (g1 - g2, g2, '%d:%d' % (g1, g2)))

    return res[-1]
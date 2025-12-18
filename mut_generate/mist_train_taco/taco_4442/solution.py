"""
QUESTION:
Two teams meet in The Game World Championship. Some scientists consider this game to be the most intellectually challenging game in the world. You are given two strings describing the teams' actions in the final battle. Figure out who became the champion.

Input

The input contains two strings of equal length (between 2 and 20 characters, inclusive). Each line describes the actions of one team.

Output

Output "TEAM 1 WINS" if the first team won, "TEAM 2 WINS" if the second team won, and "TIE" if there was a tie.

Examples

Input

[]()[]8&lt;
8&lt;[]()8&lt;


Output

TEAM 2 WINS


Input

8&lt;8&lt;()
[]8&lt;[]


Output

TIE
"""

def determine_champion(team1_actions: str, team2_actions: str) -> str:
    plays = ['()', '[]', '8<']
    w = 0
    
    for i in range(0, len(team1_actions) // 2):
        m = plays.index(team1_actions[2 * i:2 * i + 2])
        n = plays.index(team2_actions[2 * i:2 * i + 2])
        
        if m == n + 1 or m == n - 2:
            w += 1
        if m == n + 2 or m == n - 1:
            w -= 1
    
    if w > 0:
        return 'TEAM 1 WINS'
    elif w == 0:
        return 'TIE'
    else:
        return 'TEAM 2 WINS'
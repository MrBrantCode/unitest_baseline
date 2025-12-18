"""
QUESTION:
It's the most hotly anticipated game of the school year - Gryffindor vs Slytherin! Write a function which returns the winning team. 

You will be given two arrays with two values. 

The first given value is the number of points scored by the team's Chasers and the second a string with a 'yes' or 'no' value if the team caught the golden snitch!

The team who catches the snitch wins their team an extra 150 points - but doesn't always win them the game.

If the score is a tie return "It's a draw!""

** The game only ends when someone catches the golden snitch, so one array will always include 'yes' or 'no.' Points scored by Chasers can be any positive integer.
"""

def determine_winner(gryffindor, slytherin):
    # Calculate total points for Gryffindor
    gryffindor_points = gryffindor[0] + 150 * (gryffindor[1] == 'yes')
    
    # Calculate total points for Slytherin
    slytherin_points = slytherin[0] + 150 * (slytherin[1] == 'yes')
    
    # Determine the winner
    if gryffindor_points > slytherin_points:
        return "Gryffindor wins!"
    elif slytherin_points > gryffindor_points:
        return "Slytherin wins!"
    else:
        return "It's a draw!"
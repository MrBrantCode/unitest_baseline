"""
QUESTION:
Reducing Problems - Bug Fixing #8

Oh no! Timmy's reduce is causing problems, Timmy's goal is to calculate the two teams scores and return the winner but timmy has gotten confused and sometimes teams don't enter their scores, total the scores out of 3! Help timmy fix his program!

Return true if team 1 wins or false if team 2 wins!
"""

def determine_winner(team1=None, team2=None):
    # Handle default values
    if team1 is None:
        team1 = []
    if team2 is None:
        team2 = []
    
    # Calculate the total scores
    total_team1 = sum(team1)
    total_team2 = sum(team2)
    
    # Determine the winner
    return total_team1 > total_team2
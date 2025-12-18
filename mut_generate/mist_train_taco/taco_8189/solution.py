"""
QUESTION:
You are playing euchre and you want to know the new score after finishing a hand. There are two teams and each hand consists of 5 tricks. The team who wins the majority of the tricks will win points but the number of points varies. To determine the number of points, you must know which team called trump, how many tricks each team won, and if anyone went alone. Scoring is as follows:

For the team that called trump:

- if they win 2 or less tricks -> other team wins 2 points

- if they win 3 or 4 tricks -> 1 point

- if they don't go alone and win 5 tricks -> 2 points

- if they go alone and win 5 tricks -> 4 points

Only the team who called trump can go alone and you will notice that it only increases your points if you win all 5 tricks.


Your job is to create a method to calculate the new score. When reading the arguments, team 1 is represented by 1 and team 2 is represented by 2. All scores will be stored with this order: { team1, team2 }.
"""

def calculate_euchre_score(score, trump, alone, tricks):
    # Count the number of tricks won by the team that called trump
    tricks_won_by_trump = tricks.count(trump)
    
    # Determine the multiplier and additional points based on the number of tricks won
    multiplier = 2 if tricks_won_by_trump == 5 and alone else 1
    additional_points = 1 if tricks_won_by_trump in (3, 4) else 2
    
    # Determine the winning team
    winner = trump if tricks_won_by_trump > 2 else 3 - trump
    
    # Calculate the new scores
    new_score = [
        score[0] + (additional_points * multiplier if winner == 1 else 0),
        score[1] + (additional_points * multiplier if winner == 2 else 0)
    ]
    
    return new_score
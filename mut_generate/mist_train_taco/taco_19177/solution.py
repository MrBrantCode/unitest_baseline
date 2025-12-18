"""
QUESTION:
The winner of the card game popular in Berland "Berlogging" is determined according to the following rules. If at the end of the game there is only one player with the maximum number of points, he is the winner. The situation becomes more difficult if the number of such players is more than one. During each round a player gains or loses a particular number of points. In the course of the game the number of points is registered in the line "name score", where name is a player's name, and score is the number of points gained in this round, which is an integer number. If score is negative, this means that the player has lost in the round. So, if two or more players have the maximum number of points (say, it equals to m) at the end of the game, than wins the one of them who scored at least m points first. Initially each player has 0 points. It's guaranteed that at the end of the game at least one player has a positive number of points.

Input

The first line contains an integer number n (1 ≤ n ≤ 1000), n is the number of rounds played. Then follow n lines, containing the information about the rounds in "name score" format in chronological order, where name is a string of lower-case Latin letters with the length from 1 to 32, and score is an integer number between -1000 and 1000, inclusive.

Output

Print the name of the winner.

Examples

Input

3
mike 3
andrew 5
mike 2


Output

andrew


Input

3
andrew 3
andrew 2
mike 5


Output

andrew
"""

def determine_winner(n, rounds):
    # Dictionary to keep track of total scores
    total_scores = {}
    
    # List to keep track of rounds in chronological order
    chronological_scores = []
    
    # Process each round
    for name, score in rounds:
        score = int(score)
        chronological_scores.append((name, score))
        total_scores[name] = total_scores.get(name, 0) + score
    
    # Find the maximum score
    max_score = max(total_scores.values())
    
    # Identify players with the maximum score
    potential_winners = [name for name, score in total_scores.items() if score == max_score]
    
    # If there's only one player with the maximum score, they are the winner
    if len(potential_winners) == 1:
        return potential_winners[0]
    
    # Otherwise, determine the first player to reach the maximum score
    current_scores = {}
    for name, score in chronological_scores:
        current_scores[name] = current_scores.get(name, 0) + score
        if name in potential_winners and current_scores[name] >= max_score:
            return name

# Example usage:
# winner = determine_winner(3, [('mike', '3'), ('andrew', '5'), ('mike', '2')])
# print(winner)  # Output: andrew
"""
QUESTION:
Create a function `rock_paper_scissors` that takes two string arguments, `player1_choice` and `player2_choice`, representing the choices of two players in a game of rock-paper-scissors. The function should return a string indicating the result of the game, which can be "Player 1 wins", "Player 2 wins", or "It's a tie". The input strings should be case-insensitive and can be "rock", "paper", or "scissors".
"""

def rock_paper_scissors(player1_choice, player2_choice):
    choices = {"rock", "paper", "scissors"}
    player1_choice = player1_choice.lower()
    player2_choice = player2_choice.lower()

    if player1_choice == player2_choice:
        return "It's a tie"
    elif (player1_choice, player2_choice) in {("rock", "scissors"), ("scissors", "paper"), ("paper", "rock")}:
        return "Player 1 wins"
    else:
        return "Player 2 wins"
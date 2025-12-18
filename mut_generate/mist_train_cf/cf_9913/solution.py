"""
QUESTION:
Create a function `play_rpsls(player1, player2)` that takes two arguments `player1` and `player2`, representing the shapes formed by each player in the game of rock-paper-scissors-lizard-Spock. The function should return the result of the game in the format "Player X wins!" or "It's a tie!". The input will always be valid (i.e., one of the five shapes: "rock", "paper", "scissors", "lizard", or "Spock"). The function should be implemented without using if-else statements.
"""

def entance(player1, player2):
    outcomes = {
        ("rock", "scissors"): "Player 1 wins!",
        ("rock", "lizard"): "Player 1 wins!",
        ("paper", "rock"): "Player 1 wins!",
        ("paper", "Spock"): "Player 1 wins!",
        ("scissors", "paper"): "Player 1 wins!",
        ("scissors", "lizard"): "Player 1 wins!",
        ("lizard", "Spock"): "Player 1 wins!",
        ("lizard", "paper"): "Player 1 wins!",
        ("Spock", "rock"): "Player 1 wins!",
        ("Spock", "scissors"): "Player 1 wins!",
        ("rock", "rock"): "It's a tie!",
        ("paper", "paper"): "It's a tie!",
        ("scissors", "scissors"): "It's a tie!",
        ("lizard", "lizard"): "It's a tie!",
        ("Spock", "Spock"): "It's a tie!",
    }

    return outcomes.get((player1, player2), "Player 2 wins!")
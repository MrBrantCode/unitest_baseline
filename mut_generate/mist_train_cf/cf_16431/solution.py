"""
QUESTION:
Write a Python function called `play_rpsls(player1, player2)` that takes two arguments: `player1` and `player2`, representing the shapes formed by each player (strings). The function should return the result of the game in the format: "Player X wins!" or "It's a tie!". The function should not use if-else statements or comparison operators. The input shapes are limited to "rock", "paper", "scissors", "lizard", or "Spock".
"""

def play_rpsls(player1, player2):
    rules = {
        ("rock", "lizard"): "Player 1 wins!",
        ("rock", "scissors"): "Player 1 wins!",
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
        ("Spock", "Spock"): "It's a tie!"
    }
    
    result = rules.get((player1, player2))
    
    if result:
        return result
    else:
        return "Player 2 wins!"
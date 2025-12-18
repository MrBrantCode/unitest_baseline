"""
QUESTION:
Implement the `determine_winner` function to determine the winner of a rock-paper-scissors game. The function should take two parameters: `user_choice` and `computer_choice`, both of which can be either "rock", "paper", or "scissors". The function should return a string indicating the winner: "You win!", "Computer wins!", or "It's a tie!". The rules are as follows: rock beats scissors, scissors beats paper, paper beats rock, and if both choices are the same, it's a tie.
"""

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "scissors" and computer_choice == "paper") or (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "Computer wins!"
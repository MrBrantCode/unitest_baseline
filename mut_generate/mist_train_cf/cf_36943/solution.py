"""
QUESTION:
Implement the `play_card_game` function, which simulates a simple card game between two players. The function takes two lists of integers, each representing the drawn cards for a player, and returns the result of the game. 

The function should compare the card values based on their integer values, with higher integers representing higher card values. The player with the higher card value wins the round. If both players draw a card with the same value, it results in a tie for that round. The game continues until all cards have been drawn, and the player with the most round wins is declared the overall winner.

The function signature is `def play_card_game(player1_cards: List[int], player2_cards: List[int]) -> str`. The function should return a string indicating the result of the game: "Player 1 wins" if player 1 wins, "Player 2 wins" if player 2 wins, or "It's a tie" if the game results in a tie. Assume that the input lists contain valid integers representing the card values and that there are no duplicate cards within each player's deck.
"""

from typing import List

def play_card_game(player1_cards: List[int], player2_cards: List[int]) -> str:
    player1_wins = 0
    player2_wins = 0

    for card1, card2 in zip(player1_cards, player2_cards):
        if card1 > card2:
            player1_wins += 1
        elif card2 > card1:
            player2_wins += 1

    if player1_wins > player2_wins:
        return "Player 1 wins"
    elif player2_wins > player1_wins:
        return "Player 2 wins"
    else:
        return "It's a tie"
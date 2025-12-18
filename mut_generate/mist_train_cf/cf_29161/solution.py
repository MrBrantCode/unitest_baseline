"""
QUESTION:
Create a function named `compare_cards` that takes two lists of cards `player1` and `player2` as input, where each card is represented as a string in the format "value suit". The function should compare the last drawn card of each player and determine the winner based on the card values and suits. The card values follow the order 2 < 3 < 4 < 5 < 6 < 7 < 8 < 9 < 10 < J < Q < K < A, and the suit values follow the order H < D < C < S. If the players have an equal number of cards or if the last drawn cards are equal, the function should return "It's a tie!". If there are no cards to compare, the function should return "No cards to compare!".
"""

def compare_cards(player1, player2):
    if not player1 or not player2:
        return "No cards to compare!"

    card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    card_suits = {'H': 1, 'D': 2, 'C': 3, 'S': 4}

    last_card_player1 = player1[-1].split()
    last_card_player2 = player2[-1].split()

    value_player1, suit_player1 = last_card_player1[0], last_card_player1[1]
    value_player2, suit_player2 = last_card_player2[0], last_card_player2[1]

    if card_values[value_player1] > card_values[value_player2]:
        return "Player 1 wins!"
    elif card_values[value_player1] < card_values[value_player2]:
        return "Player 2 wins!"
    else:
        if card_suits[suit_player1] > card_suits[suit_player2]:
            return "Player 1 wins!"
        elif card_suits[suit_player1] < card_suits[suit_player2]:
            return "Player 2 wins!"
        else:
            return "It's a tie!"
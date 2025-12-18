"""
QUESTION:
Implement a function `play_card_game(player1, player2)` that takes two lists of strings as input, representing the cards held by each player. Each string represents a card in the format "rank suit" (e.g., "2 H" or "K D"). Compare the cards drawn by each player and return the result of the game as a string: "Player 1 wins", "Player 2 wins", or "It's a tie". The comparison rules are: if one player's card has a higher rank, they win the round; if both players draw cards of the same rank, it's a tie. Assume both input lists contain the same number of cards (at least 1 card each) and no duplicate cards within each player's hand.
"""

def play_card_game(player1, player2):
    card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    
    player1_score = 0
    player2_score = 0
    
    for card1, card2 in zip(player1, player2):
        rank1, suit1 = card1.split()
        rank2, suit2 = card2.split()
        
        if card_values[rank1] > card_values[rank2]:
            player1_score += 1
        elif card_values[rank2] > card_values[rank1]:
            player2_score += 1
    
    if player1_score > player2_score:
        return "Player 1 wins"
    elif player2_score > player1_score:
        return "Player 2 wins"
    else:
        return "It's a tie"
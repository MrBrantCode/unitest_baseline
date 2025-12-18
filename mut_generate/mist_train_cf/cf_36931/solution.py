"""
QUESTION:
Create a function `calculate_best_score` that takes in a list of cards (`hand`) as input, where each card is either an integer (2-10) or 'A' (ace), and returns the best possible score for the given hand. The score is calculated by summing the values of the cards, with aces potentially contributing 11 points each. However, if the total score exceeds 21, the value of the aces in the hand must be reduced to 1 to prevent busting. The function should return 0 if the final score exceeds 21.
"""

def calculate_best_score(hand):
    """
    Calculate the best possible score for the given hand.
    
    Args:
    hand (list): A list of cards where each card is either an integer (2-10) or 'A' (ace).
    
    Returns:
    int: The best possible score for the given hand.
    """
    # Initialize score and ace count
    score = 0
    ace_count = 0

    # Calculate the initial score and count the number of aces
    for card in hand:
        if card == 'A':
            score += 11
            ace_count += 1
        else:
            score += card

    # Adjust the score if it exceeds 21 and there are aces in the hand
    while score > 21 and ace_count:
        score -= 10
        ace_count -= 1

    # Return 0 if the score exceeds 21, otherwise return the score
    return score if score <= 21 else 0
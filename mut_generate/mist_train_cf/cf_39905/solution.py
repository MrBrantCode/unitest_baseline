"""
QUESTION:
Create a function `analyze_poker_hand(color_all, size_all)` that takes two lists as input: `color_all` containing the colors of the cards as strings and `size_all` containing the sizes of the cards as integers. The size of a card can range from 2 to 14, where 11 represents Jack, 12 represents Queen, 13 represents King, and 14 represents Ace. The function should return a tuple containing the type of poker hand and the highest card in the hand, based on the following rules: 
- If all cards have the same color and form a straight (consecutive sizes), it is a "Straight flush" with the highest card being the maximum size in the hand.
- If all cards have the same color but do not form a straight, it is a "Flush" with the highest card being the sum of all card sizes.
- If the above conditions are not met, the function should return "No special hand" as the poker hand type, and the highest card value is not specified.
"""

def analyze_poker_hand(color_all, size_all):
    if len(set(color_all)) == 1:  
        size_set = list(set(size_all))
        size_set.sort()

        if size_set[-1] - size_set[0] == 4:  
            return "Straight flush", max(size_all)
        else:
            return "Flush", sum(size_all)
    
    return "No special hand", None
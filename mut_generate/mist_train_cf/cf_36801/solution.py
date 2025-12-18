"""
QUESTION:
Implement the function `play_combat(deck1, deck2)` that simulates a game of combat between two players using their respective decks of cards. The function takes two lists of integers `deck1` and `deck2` as input, representing the initial decks of cards for the two players, and returns the index of the winning player (0 for player 1, 1 for player 2) after the game ends.

The function should follow these rules:
- Each round, the players draw the top card from their respective decks and compare the drawn cards.
- The player with the higher-valued card wins the round and receives both cards, placing them at the bottom of their deck (the winner's card first, followed by the loser's card).
- If the drawn cards have equal value, a "war" occurs. In a war, each player draws three additional cards from their deck and then compares the next (4th) card. The player with the higher-valued 4th card wins the war and receives all the cards that were involved in the war, placing them at the bottom of their deck.
- The game continues until one player has all the cards.

Assume that the input decks are valid and the game will always terminate. The input decks are represented as lists of integers, with each integer representing the value of a card in the deck, and the length of each deck is between 1 and 50.
"""

from typing import List

def play_combat(deck1: List[int], deck2: List[int]) -> int:
    deck1 = deck1.copy()
    deck2 = deck2.copy()

    while deck1 and deck2:
        card1 = deck1.pop(0)
        card2 = deck2.pop(0)

        if card1 > card2:
            deck1.extend([card1, card2])
        elif card2 > card1:
            deck2.extend([card2, card1])
        else:  # War
            if len(deck1) < 4 or len(deck2) < 4:
                return 0 if len(deck2) < 4 else 1

            war_cards1 = deck1[:4]
            war_cards2 = deck2[:4]
            deck1 = deck1[4:]
            deck2 = deck2[4:]

            while war_cards1[-1] == war_cards2[-1]:
                if len(deck1) < 4 or len(deck2) < 4:
                    return 0 if len(deck2) < 4 else 1

                war_cards1.extend(deck1[:4])
                war_cards2.extend(deck2[:4])
                deck1 = deck1[4:]
                deck2 = deck2[4:]

            if war_cards1[-1] > war_cards2[-1]:
                deck1.extend(war_cards1 + war_cards2)
            else:
                deck2.extend(war_cards2 + war_cards1)

    return 0 if deck1 else 1
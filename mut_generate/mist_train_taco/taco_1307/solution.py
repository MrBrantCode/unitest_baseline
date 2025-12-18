"""
QUESTION:
Vasily has a deck of cards consisting of n cards. There is an integer on each of the cards, this integer is between 1 and 100 000, inclusive. It is possible that some cards have the same integers on them.

Vasily decided to sort the cards. To do this, he repeatedly takes the top card from the deck, and if the number on it equals the minimum number written on the cards in the deck, then he places the card away. Otherwise, he puts it under the deck and takes the next card from the top, and so on. The process ends as soon as there are no cards in the deck. You can assume that Vasily always knows the minimum number written on some card in the remaining deck, but doesn't know where this card (or these cards) is.

You are to determine the total number of times Vasily takes the top card from the deck.


-----Input-----

The first line contains single integer n (1 ≤ n ≤ 100 000) — the number of cards in the deck.

The second line contains a sequence of n integers a_1, a_2, ..., a_{n} (1 ≤ a_{i} ≤ 100 000), where a_{i} is the number written on the i-th from top card in the deck.


-----Output-----

Print the total number of times Vasily takes the top card from the deck.


-----Examples-----
Input
4
6 3 1 2

Output
7

Input
1
1000

Output
1

Input
7
3 3 3 3 3 3 3

Output
7



-----Note-----

In the first example Vasily at first looks at the card with number 6 on it, puts it under the deck, then on the card with number 3, puts it under the deck, and then on the card with number 1. He places away the card with 1, because the number written on it is the minimum among the remaining cards. After that the cards from top to bottom are [2, 6, 3]. Then Vasily looks at the top card with number 2 and puts it away. After that the cards from top to bottom are [6, 3]. Then Vasily looks at card 6, puts it under the deck, then at card 3 and puts it away. Then there is only one card with number 6 on it, and Vasily looks at it and puts it away. Thus, in total Vasily looks at 7 cards.
"""

from collections import deque
import heapq

def calculate_card_draws(n, cards):
    cards_with_index = [(card, -1 * i) for i, card in enumerate(cards)]
    heapq.heapify(cards_with_index)
    
    draws = 0
    removed = 0
    
    while cards_with_index:
        prev = -1
        new_removals = 0
        current = cards_with_index[0]
        
        while cards_with_index and -1 * current[1] > prev:
            new_removals += 1
            heapq.heappop(cards_with_index)
            temp_prev = -1 * current[1]
            
            while cards_with_index and cards_with_index[0][0] == current[0] and (-1 * cards_with_index[0][1] > prev):
                current = cards_with_index[0]
                heapq.heappop(cards_with_index)
                new_removals += 1
            
            prev = temp_prev
            current = cards_with_index[0] if cards_with_index else 0
        
        draws += n - removed
        removed += new_removals
    
    return draws
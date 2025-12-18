"""
QUESTION:
Complete the function that determines the score of a hand in the card game [Blackjack](https://en.wikipedia.org/wiki/Blackjack) (aka 21).

The function receives an array of strings that represent each card in the hand (`"2"`, `"3",` ..., `"10"`, `"J"`, `"Q"`, `"K"` or `"A"`) and should return the score of the hand (integer).

~~~if:c
Note: in C the function receives a character array with the card `10` represented by the character `T`.
~~~


### Scoring rules:

Number cards count as their face value (2 through 10). Jack, Queen and King count as 10. An Ace can be counted as either 1 or 11.

Return the highest score of the cards that is less than or equal to 21. If there is no score less than or equal to 21 return the smallest score more than 21.


## Examples

```
["A"]                           ==>  11
["A", "J"]                      ==>  21
["A", "10", "A"]                ==>  12
["5", "3", "7"]                 ==>  15
["5", "4", "3", "2", "A", "K"]  ==>  25
```
"""

def calculate_blackjack_score(hand):
    # Calculate the initial score considering all Aces as 11
    score = sum((11 if card == 'A' else 10 if card in 'JQK' else int(card) for card in hand))
    
    # Adjust the score for Aces if necessary
    for _ in range(hand.count('A')):
        if score > 21:
            score -= 10
    
    return score
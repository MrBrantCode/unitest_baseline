"""
QUESTION:
Create a program that reads poker hand data and outputs the role for each. However, this issue follows the rules below.

* Poker is a competition with 5 playing cards.
* No more than 5 cards with the same number.
* There is no joker.
* Suppose you only consider the following poker roles: (The higher the number, the higher the role.)


1. No role (does not apply to any of the following)
2. One pair (two cards with the same number)
3. Two pairs (two pairs of cards with the same number)
4. Three cards (one set of three cards with the same number)
5. Straight (the numbers on 5 cards are consecutive)
However, in the case of a straight containing A, the sequence ending with A is also straight. In other words, there are two types of straights containing A: A 2 3 4 5 and 10 J Q K A. Lines that straddle A, such as J Q K A 2, are not straight. (In this case, it will be "no role").
6. Full House (one set of three cards with the same number and the other two cards with the same number)
7. Four Cards (one set of four cards with the same number)



Input

The input consists of multiple datasets. Each dataset is given in the following format:


Hand 1, Hand 2, Hand 3, Hand 4, Hand 5


In your hand, Trump's J (jack) is 11, Q (queen) is 12, K (king) is 13, A (ace) is 1, and the others are represented by their respective numbers.

The number of datasets does not exceed 50.

Output

For each dataset, output one of the highest roles you can play in your hand. Follow the output example for the notation of the role.

Example

Input

1,2,3,4,1
2,3,2,3,12
12,13,11,12,12
7,6,7,6,7
3,3,2,3,3
6,7,8,9,10
11,12,10,1,13
11,12,13,1,2


Output

one pair
two pair
three card
full house
four card
straight
straight
null
"""

def determine_poker_hand_role(hand: list) -> str:
    hand = sorted(hand)
    
    if hand.count(hand[0]) == 4 or hand.count(hand[1]) == 4:
        return 'four card'
    elif len(set(hand)) == 2:
        return 'full house'
    elif (hand[0] + 4 == hand[1] + 3 == hand[2] + 2 == hand[3] + 1 == hand[4] or
          hand == [1, 10, 11, 12, 13]):
        return 'straight'
    elif max(hand.count(hand[0]), hand.count(hand[1]), hand.count(hand[2])) == 3:
        return 'three card'
    elif len(set(hand)) == 3:
        return 'two pair'
    elif len(set(hand)) == 4:
        return 'one pair'
    else:
        return 'null'
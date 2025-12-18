"""
QUESTION:
Vasily has a deck of cards consisting of n cards. There is an integer on each of the cards, this integer is between 1 and 100 000, inclusive. It is possible that some cards have the same integers on them.

Vasily decided to sort the cards. To do this, he repeatedly takes the top card from the deck, and if the number on it equals the minimum number written on the cards in the deck, then he places the card away. Otherwise, he puts it under the deck and takes the next card from the top, and so on. The process ends as soon as there are no cards in the deck. You can assume that Vasily always knows the minimum number written on some card in the remaining deck, but doesn't know where this card (or these cards) is.

You are to determine the total number of times Vasily takes the top card from the deck.

Input

The first line contains single integer n (1 ≤ n ≤ 100 000) — the number of cards in the deck.

The second line contains a sequence of n integers a1, a2, ..., an (1 ≤ ai ≤ 100 000), where ai is the number written on the i-th from top card in the deck.

Output

Print the total number of times Vasily takes the top card from the deck.

Examples

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

Note

In the first example Vasily at first looks at the card with number 6 on it, puts it under the deck, then on the card with number 3, puts it under the deck, and then on the card with number 1. He places away the card with 1, because the number written on it is the minimum among the remaining cards. After that the cards from top to bottom are [2, 6, 3]. Then Vasily looks at the top card with number 2 and puts it away. After that the cards from top to bottom are [6, 3]. Then Vasily looks at card 6, puts it under the deck, then at card 3 and puts it away. Then there is only one card with number 6 on it, and Vasily looks at it and puts it away. Thus, in total Vasily looks at 7 cards.
"""

def count_card_draws(n, a):
    sorted_arr = [(i, elem) for (i, elem) in enumerate(a)]
    sorted_arr.sort(key=lambda x: (x[1], x[0]))
    sorted_indexes = [x[0] for x in sorted_arr]
    
    cnt = 0
    current_n = n
    prev_index = sorted_indexes[0]
    prev_elem = sorted_arr[0][1]
    cur_len = 1
    i = 1
    
    while i < n:
        cur_index = sorted_indexes[i]
        cur_elem = sorted_arr[i][1]
        
        if prev_index < cur_index:
            cur_len += 1
            prev_index = sorted_indexes[i]
            prev_elem = sorted_arr[i][1]
        elif i + 1 < n and cur_elem == sorted_arr[i + 1][1]:
            penalty = 1
            last_penalty_ind = sorted_indexes[i]
            while i + 1 < n and sorted_arr[i + 1][1] == cur_elem:
                if sorted_arr[i + 1][0] >= prev_index:
                    cur_len += 1
                else:
                    penalty += 1
                    last_penalty_ind = sorted_indexes[i + 1]
                i += 1
            cnt += current_n
            current_n -= cur_len
            cur_len = penalty
            prev_elem = cur_elem
            prev_index = last_penalty_ind
        else:
            cnt += current_n
            current_n -= cur_len
            cur_len = 1
            prev_index = sorted_indexes[i]
            prev_elem = sorted_arr[i][1]
        
        i += 1
    
    cnt += current_n
    return cnt
"""
QUESTION:
Catherine has a deck of n cards, each of which is either red, green, or blue. As long as there are at least two cards left, she can do one of two actions:   take any two (not necessarily adjacent) cards with different colors and exchange them for a new card of the third color;  take any two (not necessarily adjacent) cards with the same color and exchange them for a new card with that color. 

She repeats this process until there is only one card left. What are the possible colors for the final card?


-----Input-----

The first line of the input contains a single integer n (1 ≤ n ≤ 200) — the total number of cards.

The next line contains a string s of length n — the colors of the cards. s contains only the characters 'B', 'G', and 'R', representing blue, green, and red, respectively.


-----Output-----

Print a single string of up to three characters — the possible colors of the final card (using the same symbols as the input) in alphabetical order.


-----Examples-----
Input
2
RB

Output
G

Input
3
GRG

Output
BR

Input
5
BBBBB

Output
B



-----Note-----

In the first sample, Catherine has one red card and one blue card, which she must exchange for a green card.

In the second sample, Catherine has two green cards and one red card. She has two options: she can exchange the two green cards for a green card, then exchange the new green card and the red card for a blue card. Alternatively, she can exchange a green and a red card for a blue card, then exchange the blue card and remaining green card for a red card.

In the third sample, Catherine only has blue cards, so she can only exchange them for more blue cards.
"""

def possible_final_card_colors(n, s):
    r = s.count('R')
    g = s.count('G')
    b = s.count('B')
    
    colornum = 0
    if r:
        colornum += 1
    if g:
        colornum += 1
    if b:
        colornum += 1
    
    if colornum == 3:
        return 'BGR'
    elif colornum == 2:
        if r == 1:
            if b == 1:
                return 'G'
            elif b > 1:
                return 'GR'
            elif g == 1:
                return 'B'
            elif g > 1:
                return 'BR'
        elif g == 1:
            if r == 1:
                return 'B'
            elif b == 1:
                return 'R'
            elif r > 1:
                return 'BG'
            elif b > 1:
                return 'GR'
        elif b == 1:
            if r == 1:
                return 'G'
            elif g == 1:
                return 'R'
            elif r > 1:
                return 'BG'
            elif g > 1:
                return 'BR'
        else:
            return 'BGR'
    elif r:
        return 'R'
    elif g:
        return 'G'
    elif b:
        return 'B'
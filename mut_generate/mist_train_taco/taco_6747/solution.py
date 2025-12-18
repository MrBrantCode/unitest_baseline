"""
QUESTION:
Taro and Hanako are playing card games. They have n cards each, and they compete n turns. At each turn Taro and Hanako respectively puts out a card. The name of the animal consisting of alphabetical letters is written on each card, and the bigger one in lexicographical order becomes the winner of that turn. The winner obtains 3 points. In the case of a draw, they obtain 1 point each.

Write a program which reads a sequence of cards Taro and Hanako have and reports the final scores of the game.

Constraints

* n ≤ 1000
* The length of the string ≤ 100

Input

In the first line, the number of cards n is given. In the following n lines, the cards for n turns are given respectively. For each line, the first string represents the Taro's card and the second one represents Hanako's card.

Output

Print the final scores of Taro and Hanako respectively. Put a single space character between them.

Example

Input

3
cat dog
fish fish
lion tiger


Output

1 7
"""

def calculate_final_scores(n, cards):
    t = 0
    h = 0
    for tc, hc in cards:
        if tc > hc:
            t += 3
        elif tc < hc:
            h += 3
        else:
            t += 1
            h += 1
    return t, h
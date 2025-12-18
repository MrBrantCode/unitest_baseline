"""
QUESTION:
Sereja and Dima play a game. The rules of the game are very simple. The players have n cards in a row. Each card contains a number, all numbers on the cards are distinct. The players take turns, Sereja moves first. During his turn a player can take one card: either the leftmost card in a row, or the rightmost one. The game ends when there is no more cards. The player who has the maximum sum of numbers on his cards by the end of the game, wins.

Sereja and Dima are being greedy. Each of them chooses the card with the larger number during his move.

Inna is a friend of Sereja and Dima. She knows which strategy the guys are using, so she wants to determine the final score, given the initial state of the game. Help her.


-----Input-----

The first line contains integer n (1 ≤ n ≤ 1000) — the number of cards on the table. The second line contains space-separated numbers on the cards from left to right. The numbers on the cards are distinct integers from 1 to 1000.


-----Output-----

On a single line, print two integers. The first number is the number of Sereja's points at the end of the game, the second number is the number of Dima's points at the end of the game.


-----Examples-----
Input
4
4 1 2 10

Output
12 5

Input
7
1 2 3 4 5 6 7

Output
16 12



-----Note-----

In the first sample Sereja will take cards with numbers 10 and 2, so Sereja's sum is 12. Dima will take cards with numbers 4 and 1, so Dima's sum is 5.
"""

def calculate_final_scores(n, cards):
    """
    Calculate the final scores for Sereja and Dima after playing the card game.

    Parameters:
    n (int): The number of cards.
    cards (list of int): A list of integers representing the values on the cards.

    Returns:
    tuple: A tuple containing two integers, the first being Sereja's score and the second being Dima's score.
    """
    r1 = 0  # Sereja's score
    r2 = 0  # Dima's score
    t = 0   # Turn indicator: 0 for Sereja, 1 for Dima
    
    while len(cards) != 0:
        temp = max((cards[0], cards[-1]))
        i = 0 if temp == cards[0] else len(cards) - 1
        
        if t == 0:
            r1 += temp
            t = 1
        else:
            r2 += temp
            t = 0
        
        cards.pop(i)
    
    return r1, r2
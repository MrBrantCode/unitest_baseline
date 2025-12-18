"""
QUESTION:
Design an algorithm for a game where five elements (rock, paper, scissors, lizard, spock) compete against each other. Each element wins against two others and loses against the remaining two. Create a function `game(p1, p2)` that takes two player moves as input and returns the outcome of a single round, where `p1` and `p2` are one of 'rock', 'paper', 'scissors', 'lizard', or 'spock'. The function should follow the rules: 
1. Scissors cuts Paper 
2. Paper covers Rock 
3. Rock crushes Lizard 
4. Lizard poisons Spock 
5. Spock smashes Scissors 
6. Scissors decapitates Lizard 
7. Lizard eats Paper 
8. Paper disproves Spock 
9. Spock vaporizes Rock 
10. Rock crushes Scissors.
"""

def game(p1, p2):
    if p1 == p2:
        return "It's a tie!"
    rules = {'rock': ['scissors', 'lizard'], 'scissors': ['paper', 'lizard'], 'paper': ['rock', 'spock'], 
             'lizard': ['spock', 'paper'], 'spock': ['scissors', 'rock']}
    if p2.lower() in rules[p1.lower()]:
        return 'Player 1 wins!'
    else:
        return 'Player 2 wins!'
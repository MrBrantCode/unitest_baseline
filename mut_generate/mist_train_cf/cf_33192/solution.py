"""
QUESTION:
Implement a function `bullet2Movement(bullet2X, bullet2Y)` to move player 2's bullets horizontally and vertically. Also, ensure that both players' characters do not move beyond certain boundaries on the screen. The boundaries for player 1's character are such that its vertical position (`player1Y`) should not be less than 70.
"""

def bullet2Movement(bullet2X, bullet2Y):
    bullet2X += 1  # Move the bullet horizontally
    bullet2Y -= 1  # Move the bullet upwards
    return bullet2X, bullet2Y
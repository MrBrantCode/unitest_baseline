"""
QUESTION:
Write a program which reads the two dices constructed in the same way as Dice I, and determines whether these two dices are identical. You can roll a dice in the same way as Dice I, and if all integers observed from the six directions are the same as that of another dice, these dices can be considered as identical.

Constraints

* $0 \leq $ the integer assigned to a face $ \leq 100$

Input

In the first line, six integers assigned to faces of a dice are given in ascending order of their corresponding labels.
In the second line, six integers assigned to faces of another dice are given in ascending order of their corresponding labels.

Output

Print "Yes" if two dices are identical, otherwise "No" in a line.

Examples

Input

1 2 3 4 5 6
6 2 4 3 5 1


Output

Yes


Input

1 2 3 4 5 6
6 5 4 3 2 1


Output

No
"""

def are_dices_identical(dice1, dice2):
    roll_dict = dict(E=(3, 1, 0, 5, 4, 2), W=(2, 1, 5, 0, 4, 3), S=(4, 0, 2, 3, 5, 1), N=(1, 5, 2, 3, 0, 4))
    
    def roll_dice(dice, direction):
        return [dice[roll_dict[direction][i]] for i in range(6)]
    
    def rotate_dice(dice):
        return [dice[roll_dict['E'][i]] for i in range(6)]
    
    dices = [dice1]
    
    for i in 'EWSN':
        new_dice = roll_dice(dices[0], i)
        dices.append(new_dice)
    
    for _ in range(3):
        new_dice = rotate_dice(dices[-1])
        dices.append(new_dice)
    
    for dice in dices:
        if dice[0] == dice2[0] and dice[5] == dice2[5]:
            str_dice1 = ''.join(map(str, dice))
            str_dice2 = ''.join(map(str, dice2))
            side1 = str_dice1[1:3] + str_dice1[4] + str_dice1[3]
            side1 += side1
            side2 = str_dice2[1:3] + str_dice2[4] + str_dice2[3]
            if side2 in side1:
                return "Yes"
    
    return "No"
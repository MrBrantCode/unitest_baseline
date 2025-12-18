"""
QUESTION:
Write a program which reads $n$ dices constructed in the same way as Dice I, and determines whether they are all different. For the determination, use the same way as Dice III.

Constraints

* $2 \leq n \leq 100$
* $0 \leq $ the integer assigned to a face $ \leq 100$

Input

In the first line, the number of dices $n$ is given. In the following $n$ lines, six integers assigned to the dice faces are given respectively in the same way as Dice III.

Output

Print "Yes" if given dices are all different, otherwise "No" in a line.

Examples

Input

3
1 2 3 4 5 6
6 2 4 3 5 1
6 5 4 3 2 1


Output

No


Input

3
1 2 3 4 5 6
6 5 4 3 2 1
5 4 3 2 1 6


Output

Yes
"""

def are_dices_unique(dices):
    def diffDice(orgDice, newDice):
        ptn = [[1, 2, 3, 4, 5, 6], [2, 6, 3, 4, 1, 5], [3, 6, 5, 2, 1, 4], [4, 6, 2, 5, 1, 3], [5, 6, 4, 3, 1, 2], [6, 2, 4, 3, 5, 1]]
        flg = False
        tmpDice = [0, 0, 0, 0, 0, 0]
        for i in range(6):
            for (idx, j) in enumerate(ptn[i]):
                tmpDice[idx] = newDice[j - 1]
            if orgDice[0] != tmpDice[0] and orgDice[5] != tmpDice[5]:
                continue
            if orgDice[0] == tmpDice[0] and orgDice[5] != tmpDice[5] or (orgDice[0] != tmpDice[0] and orgDice[5] == tmpDice[5]):
                continue
            if orgDice[1:5] == [tmpDice[1], tmpDice[2], tmpDice[3], tmpDice[4]] or orgDice[1:5] == [tmpDice[3], tmpDice[1], tmpDice[4], tmpDice[2]] or orgDice[1:5] == [tmpDice[2], tmpDice[4], tmpDice[1], tmpDice[3]] or (orgDice[1:5] == [tmpDice[4], tmpDice[3], tmpDice[2], tmpDice[1]]):
                flg = True
                break
        return flg

    n = len(dices)
    for i in range(1, n):
        if diffDice(dices[0], dices[i]):
            return False
    return True
"""
QUESTION:
<image>


There used to be a game called Joseph's potatoes. Let's say n people are participating. Participants form a circle facing the center and are numbered starting from 1. One hot potato is given to participant n (the large number 30 inside the figure on the left). Participants who are given the potatoes will give the potatoes to the participant on the right. The person passed the mth time is passed to the person on the right and exits the circle (the figure on the left shows the case of m = 9). Each time you hand it over, you will pass one by one, and the last remaining person will be the winner and you will receive potatoes.

After n and m are decided, it would be nice to know where you can win before you actually start handing the potatoes. The figure above shows the case of playing this game with the rule that 30 participants exit every 9 people. The large numbers on the inside are the numbers assigned to the participants, and the small numbers on the outside are the numbers that are removed. According to it, it will break out of the circle in the order of 9,18,27,6,16,26, and 21 will remain at the end. That is, 21 is the winner (the smaller number is 30).

Enter the number of game participants n and the interval m between the participants who break out of the circle, and create a program that outputs the winner's number. However, m, n <1000.



input

Given multiple datasets. Each dataset is given in the following format:


n m


The number of game participants n (integer) and the interval m (integer) between the participants who break out of the circle are given on one line separated by blanks.

The input ends with two 0s. The number of datasets does not exceed 50.

output

For each dataset, output the number (integer) of the winner and the person who will receive the potatoes on one line.

Example

Input

41 3
30 9
0 0


Output

31
21
"""

def find_josephus_winner(n: int, m: int) -> int:
    if n == 0 or m == 0:
        return 0
    
    a = m - 1
    while a < (m - 1) * n:
        a = m * a // (m - 1) + 1
    a = n * m - a
    return a
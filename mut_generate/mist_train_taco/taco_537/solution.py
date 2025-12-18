"""
QUESTION:
Many of us are familiar with collatz sequence. Know the problem is, There is a fight going between the students of the class they have splitted up into two groups the odd rulers and the even rulers. To resolve this fight sir will randomly pick up the numbers and are written on the board. Teacher stated that if the total sum of all even numbers occuring in the collatz sequence for a number when it is divided by the total no of steps to reach 1 remainder is named as odd remainder will be compared with  the even remainder i.e., sum of all odd numbers in sequence divided with steps the resulting remainder. If the odd remainder is greater than even then odd rulers win, if even remainder is more than odd remainder then even rulers win. if both are same then there is a tie.

INPUT:
First line contains number of test cases T.
Next T line contains a number N for each line
OUTPUT:
for every respective N print either "Even Rules" or "Odd Rules" or "Tie" according to the problem.

Explanation:
for n=4, steps followed are 4->2->1 no of steps is 2 and even sum is 6 and odd sum is 1  since 6%2 < 1%2 so Odd Rules

SAMPLE INPUT
2
3
4

SAMPLE OUTPUT
Even Rules
Odd Rules
"""

def determine_winner(N):
    oddsum = 1
    evensum = 0
    totsteps = 0
    
    num = N
    while num > 1:
        if num % 2 == 0:
            evensum += num
            num //= 2
        else:
            oddsum += num
            num = (3 * num) + 1
        totsteps += 1
    
    evenrem = evensum % totsteps
    oddrem = oddsum % totsteps
    
    if oddrem > evenrem:
        return "Odd Rules"
    elif oddrem < evenrem:
        return "Even Rules"
    else:
        return "Tie"
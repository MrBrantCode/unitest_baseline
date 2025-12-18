"""
QUESTION:
problem

JOI, who has been suffering from his winter vacation homework every time, decided to do his homework systematically this time. Homework is a national language and math drill, with a national language drill on page A and a math drill on page B.

JOI can advance the Japanese drill up to C pages and the math drill up to D pages a day, but if he does his homework, he can't play that day.

There are L days during the winter vacation, and JOI must finish his homework during the winter vacation. Create a program that asks how many days JOI can play during the winter vacation.



input

The input consists of 5 lines, with one positive integer written on each line.

The integer L (2 ≤ L ≤ 40) is written on the first line, which indicates the number of days of winter vacation.

The integer A (1 ≤ A ≤ 1000) is written on the second line, which indicates the number of pages of the Japanese drill.

The integer B (1 ≤ B ≤ 1000) is written on the third line, which indicates the number of pages of the math drill.

The integer C (1 ≤ C ≤ 100) is written on the 4th line, which indicates the maximum number of pages of a national language drill that JOI can advance in a day.

The integer D (1 ≤ D ≤ 100) is written on the 5th line, which indicates the maximum number of pages of the math drill that JOI can advance in a day.

However, given the input data, JOI is guaranteed to be able to finish his homework during the winter vacation and play for at least a day.

Example

Input

20
25
30
6
8


Output

15
"""

def calculate_play_days(L, A, B, C, D):
    # Calculate the number of days required to finish the Japanese drill
    if A % C == 0:
        days_for_japanese = A // C
    else:
        days_for_japanese = A // C + 1
    
    # Calculate the number of days required to finish the math drill
    if B % D == 0:
        days_for_math = B // D
    else:
        days_for_math = B // D + 1
    
    # The total number of days required to finish both drills
    total_days_required = max(days_for_japanese, days_for_math)
    
    # The number of days JOI can play is the total vacation days minus the days required for homework
    days_to_play = L - total_days_required
    
    return days_to_play
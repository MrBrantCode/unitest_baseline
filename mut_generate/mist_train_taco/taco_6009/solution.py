"""
QUESTION:
Mohan and his friends got bore so they decided to play something which help them to improve their Mental Math as exams are near by.So all of them frame their own questions  for the game.
But when Mohan asked his question none his friends was able to answer it 
so now they asked you for the help you have to tell the largest Factor/Divisor for the given number if it exits.

INPUT
First line will be the number of T  Testcases
followed by T lines with 2 number and the remainder separated by  space.

OUTPUT
Print the largest Factor/Divisor.

SAMPLE INPUT
1
8 4 0 0

SAMPLE OUTPUT
4

Explanation

So here are total 1 testcase
and two numbers are  8 and 4 and there remainder is 0 for 8 and 
0 for 4 so the largest factor is 4 for both numbers.
"""

def find_largest_factor(a, b, ar, br):
    # Adjust the numbers by subtracting the remainders
    a = a - ar
    b = b - br
    
    # Determine the smaller of the two adjusted numbers
    if a < b:
        t = a
    else:
        t = b
    
    # Find the largest factor that divides both adjusted numbers
    while True:
        if b % t == 0 and a % t == 0:
            break
        t = t - 1
    
    return t
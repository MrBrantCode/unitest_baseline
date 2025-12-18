"""
QUESTION:
In a coordinate system,There are 3 chocolate which will be placed at three random position (x1,y1),(x2,y2) and (x3,y3).Ramesh loves Chocolates. Ramesh always moves along a straight line. your task is to find out whether he can have all the chocolates.

Input Format :-
The first line of the input contains an integer T denoting the number of test cases. Each of the next T lines contains coordinates in integer- x1 y1 x2 y2 and x3 y3.

Output Format :-
If Ramesh can get all chocolates then print "YES" otherwise "NO"(without quotes).

Constraints :-
1 ≤ T ≤ 100
-1000 ≤ x1,y1,x2,y2,x3,y3 ≤ 1000

SAMPLE INPUT
2
1 1 2 2 3 3
1 2 5 4 10 15

SAMPLE OUTPUT
YES
NO
"""

def can_ramesh_get_all_chocolates(x1, y1, x2, y2, x3, y3):
    result1 = (y2 - y1) * (x3 - x2)
    result2 = (y3 - y2) * (x2 - x1)
    
    if result1 == result2:
        return "YES"
    else:
        return "NO"
"""
QUESTION:
Problem statement:

Kiran P.S wrote some text on a piece of paper and now he wants to know 
how many star characters are in the text. 
If you think of the paper as the plane and a letter as a curve on the plane, then each letter divides the plane into regions. For example letters "A", "D", "O", "P", "R" divide
 the plane into two regions so we say these letters each have one hole.
 Similarly, letter "B" has two holes and letters such as "C", "E", "F", "K"
 have no star character.  We say that the number of holes in the text is equal to the total number of holes in the letters of the text.. Help Kiran P.S. to 
determine what is the difference in number of holes in the upper and lower case
representation of a given string.

Input

The first line contains a single integer T ≤ 40, the number of test cases. T test cases follow.
The only line of each test case contains a non-empty text composed only 
of uppercase letters of English alphabet. The length of the text is less then 100.

Output

For each test case, output a single line containing the difference of holes each text case.

SAMPLE INPUT
2
HACKEREARTH
THENATIONALINSTITUTEOFENGINEERING

SAMPLE OUTPUT
0
-6
"""

def calculate_hole_difference(text: str) -> int:
    upper_holes = {'A': 1, 'B': 2, 'D': 1, 'O': 1, 'P': 1, 'Q': 1, 'R': 1}
    lower_holes = {'a': 1, 'b': 1, 'd': 1, 'e': 0, 'g': 0, 'o': 1, 'p': 1, 'q': 1}
    
    holes = 0
    lo = text.lower()
    
    for i in range(len(text)):
        if text[i] in upper_holes:
            holes += upper_holes[text[i]]
        if lo[i] in lower_holes:
            holes -= lower_holes[lo[i]]
    
    return holes
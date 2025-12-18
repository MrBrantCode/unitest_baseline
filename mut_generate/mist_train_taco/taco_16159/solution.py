"""
QUESTION:
Chef develops his own computer program for playing chess. He is at the very beginning. At first he needs to write the module that will receive moves written by the players and analyze it. The module will receive a string and it should report at first whether this string represents the correct pair of cells on the chess board (we call such strings correct) and then report whether it represents the correct move depending on the situation on the chess board. Chef always has troubles with analyzing knight moves. So at first he needs a test program that can say whether a given string is correct and then whether it represents a correct knight move (irregardless of the situation on the chess board). The cell on the chessboard is represented as a string of two characters: first character is a lowercase Latin letter from a to h and the second character is a digit from 1 to 8. The string represents the correct pair of cells on the chess board if it composed of 5 characters where first two characters represent the cell where chess figure was, 3rd character is the dash "-" and the last two characters represent the destination cell.

-----Input-----
The first line contains a single integer T <= 50000, the number of test cases. T test cases follow. The only line of each test case contains a non-empty string composed the characters with ASCII-codes from 32 to 126. The length of the string is not greater than 10.

-----Output-----
For each test case, output a single line containing the word "Error" if the corresponding string does not represent the correct pair of cells on the chess board. Otherwise output "Yes" if this pair of cells represents the correct knight move and "No" otherwise.

-----Example-----
Input:
4
a1-b3
d2-h8
a3 c4
ErrorError

Output:
Yes
No
Error
Error
"""

def is_valid_knight_move(move: str) -> str:
    def gc(c: str) -> bool:
        return 'a' <= c <= 'h'

    def gd(c: str) -> bool:
        return '1' <= c <= '8'

    if len(move) != 5:
        return 'Error'
    
    if move[2] != '-':
        return 'Error'
    
    x1, y1, x2, y2 = move[0], move[1], move[3], move[4]
    
    if gc(x1) and gd(y1) and gc(x2) and gd(y2):
        d1 = abs(ord(x1) - ord(x2))
        d2 = abs(ord(y1) - ord(y2))
        
        if d1 > d2:
            d1, d2 = d2, d1
        
        if d1 == 1 and d2 == 2:
            return 'Yes'
        else:
            return 'No'
    else:
        return 'Error'
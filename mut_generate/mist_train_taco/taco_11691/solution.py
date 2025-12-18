"""
QUESTION:
Sitting in a station waiting room, Joisino is gazing at her train ticket.
The ticket is numbered with four digits A, B, C and D in this order, each between 0 and 9 (inclusive).
In the formula A op1 B op2 C op3 D = 7, replace each of the symbols op1, op2 and op3 with + or - so that the formula holds.
The given input guarantees that there is a solution. If there are multiple solutions, any of them will be accepted.

-----Constraints-----
 - 0≤A,B,C,D≤9
 - All input values are integers.
 - It is guaranteed that there is a solution.

-----Input-----
Input is given from Standard Input in the following format:
ABCD

-----Output-----
Print the formula you made, including the part =7.
Use the signs + and -.
Do not print a space between a digit and a sign.

-----Sample Input-----
1222

-----Sample Output-----
1+2+2+2=7

This is the only valid solution.
"""

def find_equation_for_seven(ticket_number: str) -> str:
    N = [int(i) for i in ticket_number]
    
    for i in range(8):
        binary_str = format(i, '03b')
        ans = N[0]
        msg = str(N[0])
        
        for j in range(3):
            if binary_str[j] == '0':
                ans += N[j + 1]
                msg += '+' + str(N[j + 1])
            else:
                ans -= N[j + 1]
                msg += '-' + str(N[j + 1])
        
        if ans == 7:
            return msg + '=7'

    # If no solution is found (which should not happen due to problem constraints)
    return ""
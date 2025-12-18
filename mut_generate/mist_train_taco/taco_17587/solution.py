"""
QUESTION:
You have decided to give an allowance to your child depending on the outcome of the game that he will play now.
The game is played as follows:
 - There are three "integer panels", each with a digit between 1 and 9 (inclusive) printed on it, and one "operator panel" with a + printed on it.
 - The player should construct a formula of the form X + Y, by arranging the four panels from left to right. (The operator panel should not be placed at either end of the formula.)
 - Then, the amount of the allowance will be equal to the resulting value of the formula.
Given the values A, B and C printed on the integer panels used in the game, find the maximum possible amount of the allowance.

-----Constraints-----
 - All values in input are integers.
 - 1 \leq A, B, C \leq 9

-----Input-----
Input is given from Standard Input in the following format:
A B C

-----Output-----
Print the maximum possible amount of the allowance.

-----Sample Input-----
1 5 2

-----Sample Output-----
53

The amount of the allowance will be 53 when the panels are arranged as 52+1, and this is the maximum possible amount.
"""

def calculate_maximum_allowance(A: int, B: int, C: int) -> int:
    # Sort the digits to find the maximum possible arrangement
    digits = sorted([A, B, C])
    
    # Construct the maximum possible formula by placing the largest two digits on the left
    # and the smallest digit on the right of the operator
    max_formula = f"{digits[2]}{digits[1]}+{digits[0]}"
    
    # Evaluate the formula to get the maximum allowance
    max_allowance = eval(max_formula)
    
    return max_allowance
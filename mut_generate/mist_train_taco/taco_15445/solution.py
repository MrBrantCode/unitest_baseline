"""
QUESTION:
In recreational mathematics, a magic square is an arrangement of distinct numbers (i.e., each number is used once), usually integers, in a square grid, where the numbers in each row, and in each column, and the numbers in the main and secondary diagonals, all add up to the same number, called the "magic constant."

For example, the following "square":

      4    9    2 -> 15
      3    5    7 -> 15
      8    1    6 -> 15
     /v    v    v \
    15 15   15   15  15
    
A 3x3 magic square will have its sums always resulting to 15, this number is called the "magic constant" and changes according to the square size.

In this problem you will have to create a function that receives a 3x3 'square' and returns True if it is magic and False otherwise.
The sum of rows, columns or diagonals should **always** equal **15**.

For example, the above square will be passed like: `[4, 9, 2, 3, 5, 7, 8, 1, 6]` and the output should be True

`[9, 4, 7, 3, 5, 2, 8, 6, 1]` should return False

### Note:
This kata is very easy. If you want to try some more "difficult" ones you may try these :
* [Magic Square - Verify 3x3](https://www.codewars.com/kata/magic-square-verify-3x3)
* [Double Even Magic Square](https://www.codewars.com/kata/double-even-magic-square)
* [Odd Magic Square](https://www.codewars.com/kata/odd-magic-square)
"""

def is_magic_square(square):
    # Check if the input list has exactly 9 elements
    if len(square) != 9:
        return False
    
    # Define the magic constant for a 3x3 magic square
    magic_constant = 15
    
    # Calculate the sums of rows, columns, and diagonals
    row1 = sum(square[0:3])
    row2 = sum(square[3:6])
    row3 = sum(square[6:9])
    col1 = sum(square[0::3])
    col2 = sum(square[1::3])
    col3 = sum(square[2::3])
    diag1 = sum(square[0::4])
    diag2 = sum(square[2:7:2])
    
    # Check if all sums are equal to the magic constant
    return (row1 == row2 == row3 == col1 == col2 == col3 == diag1 == diag2 == magic_constant)
"""
QUESTION:
If Give an integer N . Write a program to obtain the sum of the first and last digits of this number.

-----Input-----

The first line contains an integer T, the total number of test cases. Then follow T lines, each line contains an integer N. 

-----Output-----
For each test case, display the sum of first and last digits of N in a new line.

-----Constraints-----
- 1 ≤ T ≤ 1000
- 1 ≤ N ≤ 1000000

-----Example-----
Input
3 
1234
124894
242323

Output
5
5
5
"""

def sum_of_first_and_last_digit(N: int) -> int:
    # Convert the number to a string to easily access the first and last digits
    str_N = str(N)
    
    # Get the first and last digits
    first_digit = int(str_N[0])
    last_digit = int(str_N[-1])
    
    # Return their sum
    return first_digit + last_digit
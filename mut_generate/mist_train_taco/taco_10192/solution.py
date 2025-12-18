"""
QUESTION:
You are given a three-digit positive integer N.

Determine whether N is a palindromic number.

Here, a palindromic number is an integer that reads the same backward as forward in decimal notation.

-----Constraints-----
 - 100≤N≤999
 - N is an integer.

-----Input-----
Input is given from Standard Input in the following format:  
N

-----Output-----
If N is a palindromic number, print Yes; otherwise, print No.

-----Sample Input-----
575

-----Sample Output-----
Yes

N=575 is also 575 when read backward, so it is a palindromic number. You should print Yes.
"""

def is_palindromic_number(N: int) -> str:
    # Convert the integer to a string to easily check the first and last characters
    str_N = str(N)
    
    # Check if the first and last characters are the same
    if str_N[0] == str_N[-1]:
        return 'Yes'
    else:
        return 'No'
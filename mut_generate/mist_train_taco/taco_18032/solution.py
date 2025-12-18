"""
QUESTION:
It is September 9 in Japan now.
You are given a two-digit integer N. Answer the question: Is 9 contained in the decimal notation of N?

-----Constraints-----
 - 10≤N≤99

-----Input-----
Input is given from Standard Input in the following format:
N

-----Output-----
If 9 is contained in the decimal notation of N, print Yes; if not, print No.

-----Sample Input-----
29

-----Sample Output-----
Yes

The one's digit of 29 is 9.
"""

def contains_digit_nine(N: int) -> str:
    """
    Determines if the digit 9 is contained in the decimal notation of a given two-digit integer N.

    Parameters:
    N (int): A two-digit integer (10 ≤ N ≤ 99).

    Returns:
    str: 'Yes' if the digit 9 is contained in N, otherwise 'No'.
    """
    if '9' in str(N):
        return 'Yes'
    else:
        return 'No'
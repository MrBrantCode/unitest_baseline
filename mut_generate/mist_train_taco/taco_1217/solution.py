"""
QUESTION:
Three people, A, B and C, are trying to communicate using transceivers.
They are standing along a number line, and the coordinates of A, B and C are a, b and c (in meters), respectively.
Two people can directly communicate when the distance between them is at most d meters.
Determine if A and C can communicate, either directly or indirectly.
Here, A and C can indirectly communicate when A and B can directly communicate and also B and C can directly communicate.

-----Constraints-----
 - 1 ≤ a,b,c ≤ 100
 - 1 ≤ d ≤ 100
 - All values in input are integers.

-----Input-----
Input is given from Standard Input in the following format:
a b c d

-----Output-----
If A and C can communicate, print Yes; if they cannot, print No.

-----Sample Input-----
4 7 9 3

-----Sample Output-----
Yes

A and B can directly communicate, and also B and C can directly communicate, so we should print Yes.
"""

def can_communicate(a: int, b: int, c: int, d: int) -> str:
    """
    Determines if A and C can communicate, either directly or indirectly.

    Parameters:
    - a (int): The coordinate of person A.
    - b (int): The coordinate of person B.
    - c (int): The coordinate of person C.
    - d (int): The maximum distance within which two people can directly communicate.

    Returns:
    - str: "Yes" if A and C can communicate, "No" otherwise.
    """
    if abs(c - a) <= d:
        return "Yes"
    elif abs(a - b) <= d and abs(b - c) <= d:
        return "Yes"
    else:
        return "No"
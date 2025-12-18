"""
QUESTION:
Takahashi is going to set a 3-character password.
How many possible passwords are there if each of its characters must be a digit between 1 and N (inclusive)?

-----Constraints-----
 - 1 \leq N \leq 9
 - N is an integer.

-----Input-----
Input is given from Standard Input in the following format:
N

-----Output-----
Print the number of possible passwords.

-----Sample Input-----
2

-----Sample Output-----
8

There are eight possible passwords: 111, 112, 121, 122, 211, 212, 221, and 222.
"""

def calculate_possible_passwords(N: int) -> int:
    """
    Calculate the number of possible 3-character passwords where each character
    is a digit between 1 and N (inclusive).

    Parameters:
    N (int): The maximum digit that can be used in the password.

    Returns:
    int: The number of possible passwords.
    """
    return N * N * N
"""
QUESTION:
You are given a string S of length N consisting of A, B and C, and an integer K which is between 1 and N (inclusive).
Print the string S after lowercasing the K-th character in it.

-----Constraints-----
 - 1 ≤ N ≤ 50
 - 1 ≤ K ≤ N
 - S is a string of length N consisting of A, B and C.

-----Input-----
Input is given from Standard Input in the following format:
N K
S

-----Output-----
Print the string S after lowercasing the K-th character in it.

-----Sample Input-----
3 1
ABC

-----Sample Output-----
aBC
"""

def lowercase_kth_character(N: int, K: int, S: str) -> str:
    """
    Lowercases the K-th character in the string S and returns the modified string.

    Parameters:
    - N (int): The length of the string S.
    - K (int): The 1-based index of the character to be lowercased.
    - S (str): The input string consisting of characters 'A', 'B', and 'C'.

    Returns:
    - str: The modified string with the K-th character lowercased.
    """
    # Adjust K to be 0-based index
    K_adjusted = K - 1
    # Lowercase the K-th character and construct the new string
    modified_string = S[:K_adjusted] + S[K_adjusted].lower() + S[K_adjusted + 1:]
    return modified_string
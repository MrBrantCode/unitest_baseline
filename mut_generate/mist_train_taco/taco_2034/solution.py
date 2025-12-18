"""
QUESTION:
We have a string S of length N consisting of uppercase English letters.
How many times does ABC occur in S as contiguous subsequences (see Sample Inputs and Outputs)?

-----Constraints-----
 - 3 \leq N \leq 50
 - S consists of uppercase English letters.

-----Input-----
Input is given from Standard Input in the following format:
N
S

-----Output-----
Print number of occurrences of ABC in S as contiguous subsequences.

-----Sample Input-----
10
ZABCDBABCQ

-----Sample Output-----
2

Two contiguous subsequences of S are equal to ABC: the 2-nd through 4-th characters, and the 7-th through 9-th characters.
"""

def count_abc_subsequences(S: str, N: int = None) -> int:
    """
    Counts the number of times "ABC" occurs as a contiguous subsequence in the string S.

    Parameters:
    - S (str): The input string consisting of uppercase English letters.
    - N (int, optional): The length of the string S. If not provided, it is calculated from S.

    Returns:
    - int: The number of occurrences of "ABC" in S.
    """
    if N is None:
        N = len(S)
    
    # Ensure the length of S matches the provided N
    if N != len(S):
        raise ValueError("The length of S does not match the provided N.")
    
    # Count the occurrences of "ABC" in S
    return S.count('ABC')
"""
QUESTION:
Problem Statement 
Unseen gang is the team of most wanted criminal. Unseen gang has planted bombs in different street and corner of the city. Gang members are sitting in the other part of the city, far away from the bomb site. They are controlling the bomb by sending the activation signal in the form of encrypted code.The Enigma crew has found the solution for the encrypted code. They came to know that the code is in the form of string S. Dividing the string up to its length L into many substrings of length N will give them the location of the bomb site.

Your job is to help the Enigma crew in finding the decrypted code. So, they can track the bomb site.

Input Format
The first line contain a string S.
In the second line integer N the length of the substring is given.

Output Format
Output line contain the total number of substrings each in new line.

Constraints 
1 ≤ L ≤ 10000
1 ≤ N=20

SAMPLE INPUT
Vhaveplanted bomb @allthe location intheCITY.
8

SAMPLE OUTPUT
Vhavepla
nted bom
b @allth
e locati
on inthe
CITY.
"""

def generate_substrings(S: str, N: int) -> list[str]:
    """
    Generates substrings of length N from the input string S.

    Parameters:
    S (str): The input string to be divided into substrings.
    N (int): The length of each substring.

    Returns:
    list[str]: A list of substrings of length N.
    """
    substrings = []
    i = 0
    while i < len(S):
        substrings.append(S[i:i+N])
        i += N
    return substrings
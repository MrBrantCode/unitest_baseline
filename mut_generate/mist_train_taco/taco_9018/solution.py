"""
QUESTION:
When you asked some guy in your class his name, he called himself S, where S is a string of length between 3 and 20 (inclusive) consisting of lowercase English letters. You have decided to choose some three consecutive characters from S and make it his nickname. Print a string that is a valid nickname for him.

Constraints

* 3 \leq |S| \leq 20
* S consists of lowercase English letters.

Input

Input is given from Standard Input in the following format:


S


Output

Print your answer.

Examples

Input

takahashi


Output

tak


Input

naohiro


Output

nao
"""

def generate_nickname(S: str) -> str:
    """
    Generates a nickname by taking the first three consecutive characters from the input string S.

    Parameters:
    S (str): A string of length between 3 and 20 (inclusive) consisting of lowercase English letters.

    Returns:
    str: The first three consecutive characters of the input string S.
    """
    return S[:3]
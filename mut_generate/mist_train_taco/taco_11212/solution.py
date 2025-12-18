"""
QUESTION:
You are given three words s_1, s_2 and s_3, each composed of lowercase English letters, with spaces in between.
Print the acronym formed from the uppercased initial letters of the words.

-----Constraints-----
 - s_1, s_2 and s_3 are composed of lowercase English letters.
 - 1 ≤ |s_i| ≤ 10 (1≤i≤3)

-----Input-----
Input is given from Standard Input in the following format:
s_1 s_2 s_3

-----Output-----
Print the answer.

-----Sample Input-----
atcoder beginner contest

-----Sample Output-----
ABC

The initial letters of atcoder, beginner and contest are a, b and c. Uppercase and concatenate them to obtain ABC.
"""

def generate_acronym(s1: str, s2: str, s3: str) -> str:
    """
    Generates an acronym from the uppercased initial letters of three given words.

    Parameters:
    - s1 (str): The first word.
    - s2 (str): The second word.
    - s3 (str): The third word.

    Returns:
    - str: The acronym formed from the uppercased initial letters of the three words.
    """
    return ''.join([s1[0], s2[0], s3[0]]).upper()
"""
QUESTION:
You are given a string s consisting of lowercase English letters. Extract all the characters in the odd-indexed positions and print the string obtained by concatenating them. Here, the leftmost character is assigned the index 1.

-----Constraints-----
 - Each character in s is a lowercase English letter.
 - 1≤|s|≤10^5

-----Input-----
The input is given from Standard Input in the following format:
s

-----Output-----
Print the string obtained by concatenating all the characters in the odd-numbered positions.

-----Sample Input-----
atcoder

-----Sample Output-----
acdr

Extract the first character a, the third character c, the fifth character d and the seventh character r to obtain acdr.
"""

def extract_odd_position_chars(s: str) -> str:
    """
    Extracts and returns the characters from the odd-indexed positions of the input string `s`.
    The leftmost character is assigned the index 1.

    Parameters:
    s (str): The input string consisting of lowercase English letters.

    Returns:
    str: The string obtained by concatenating all the characters in the odd-numbered positions.
    """
    answer = str()
    for i in range(len(s)):
        if i % 2 == 0:
            answer += s[i]
    return answer
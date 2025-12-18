"""
QUESTION:
The word internationalization is sometimes abbreviated to i18n.
This comes from the fact that there are 18 letters between the first i and the last n.
You are given a string s of length at least 3 consisting of lowercase English letters.
Abbreviate s in the same way.

-----Constraints-----
 - 3 ≤ |s| ≤ 100 (|s| denotes the length of s.)
 - s consists of lowercase English letters.

-----Input-----
Input is given from Standard Input in the following format:
s

-----Output-----
Print the abbreviation of s.

-----Sample Input-----
internationalization

-----Sample Output-----
i18n
"""

def abbreviate_word(s: str) -> str:
    """
    Abbreviates a given string `s` by taking the first and last characters and 
    inserting the number of characters between them.

    Parameters:
    s (str): A string of length at least 3, consisting of lowercase English letters.

    Returns:
    str: The abbreviated form of the string.
    """
    s_len = len(s)
    head = s[0]
    tail = s[s_len - 1]
    return head + str(s_len - 2) + tail
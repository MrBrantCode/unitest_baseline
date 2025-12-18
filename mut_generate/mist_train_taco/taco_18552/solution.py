"""
QUESTION:
Let w be a string consisting of lowercase letters.
We will call w beautiful if the following condition is satisfied:
 - Each lowercase letter of the English alphabet occurs even number of times in w.
You are given the string w. Determine if w is beautiful.

-----Constraints-----
 - 1 \leq |w| \leq 100
 - w consists of lowercase letters (a-z).

-----Input-----
The input is given from Standard Input in the following format:
w

-----Output-----
Print Yes if w is beautiful. Print No otherwise.

-----Sample Input-----
abaccaba

-----Sample Output-----
Yes

a occurs four times, b occurs twice, c occurs twice and the other letters occur zero times.
"""

def is_beautiful_string(w: str) -> bool:
    """
    Determines if the given string w is beautiful.
    A string is considered beautiful if each lowercase letter of the English alphabet occurs an even number of times in w.

    Parameters:
    w (str): The input string consisting of lowercase letters.

    Returns:
    bool: True if the string is beautiful, False otherwise.
    """
    # Create a set of unique characters in the string
    unique_chars = set(w)
    
    # Check the frequency of each character
    for char in unique_chars:
        if w.count(char) % 2 != 0:
            return False
    
    return True
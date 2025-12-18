"""
QUESTION:
Sig has built his own keyboard. Designed for ultimate simplicity, this keyboard only has 3 keys on it: the 0 key, the 1 key and the backspace key.
To begin with, he is using a plain text editor with this keyboard. This editor always displays one string (possibly empty). Just after the editor is launched, this string is empty. When each key on the keyboard is pressed, the following changes occur to the string:
 - The 0 key: a letter 0 will be inserted to the right of the string.
 - The 1 key: a letter 1 will be inserted to the right of the string.
 - The backspace key: if the string is empty, nothing happens. Otherwise, the rightmost letter of the string is deleted.
Sig has launched the editor, and pressed these keys N times in total. As a result, the editor displays a string s. Find the number of such ways to press the keys, modulo 10^9 + 7.

-----Constraints-----
 - 1 ≦ N ≦ 5000
 - 1 ≦ |s| ≦ N
 - s consists of the letters 0 and 1.

-----Partial Score-----
 - 400 points will be awarded for passing the test set satisfying 1 ≦ N ≦ 300.

-----Input-----
The input is given from Standard Input in the following format:
N
s

-----Output-----
Print the number of the ways to press the keys N times in total such that the editor displays the string s in the end, modulo 10^9+7.

-----Sample Input-----
3
0

-----Sample Output-----
5

We will denote the backspace key by B. The following 5 ways to press the keys will cause the editor to display the string 0 in the end: 00B, 01B, 0B0, 1B0, BB0. In the last way, nothing will happen when the backspace key is pressed.
"""

def count_key_press_ways(N: int, s: str) -> int:
    """
    Calculate the number of ways to press the keys N times such that the editor displays the string s in the end, modulo 10^9 + 7.

    Parameters:
    - N (int): The total number of key presses.
    - s (str): The target string that should be displayed in the editor after N key presses.

    Returns:
    - int: The number of ways to achieve the target string, modulo 10^9 + 7.
    """
    MOD = 10**9 + 7
    p = [0] * 5001
    p[len(s)] = 1
    
    while N:
        p = [((2 * p[j - 1] if j else p[j]) + p[j + 1]) % MOD for j in range(N)]
        N -= 1
    
    return p[0]
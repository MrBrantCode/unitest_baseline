"""
QUESTION:
Fukushima Prefecture is also famous for producing fruits, and among them, peaches and apples boast one of the highest production volumes in Japan. By the way, when I made a print manuscript of an English pamphlet for sale, I mistakenly wrote the description about apples and the description about peaches in reverse.

You've been tasked with fixing apple and peach, but it's kind of annoying. Enter a single line of English text and create a program that outputs the English text with all the character strings apple in it replaced with peach and all the character strings peach replaced with apple.



Input

English text (including half-width alphanumeric characters, spaces, and symbols) is given on one line. The length of the string entered is 1000 or less.

Output

Outputs English sentences with the character strings apple and peach exchanged on one line.

Example

Input

the cost of one peach is higher than that of one apple.


Output

the cost of one apple is higher than that of one peach.
"""

def swap_apple_and_peach(text: str) -> str:
    """
    Swaps all occurrences of 'apple' with 'peach' and all occurrences of 'peach' with 'apple' in the given text.

    Parameters:
    text (str): The input English text.

    Returns:
    str: The modified text with 'apple' and 'peach' swapped.
    """
    a, p, t = 'apple', 'peach', '_'
    return text.replace(a, t).replace(p, a).replace(t, p)
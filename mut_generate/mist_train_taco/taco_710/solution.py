"""
QUESTION:
The Easter Rabbit laid n eggs in a circle and is about to paint them. 

Each egg should be painted one color out of 7: red, orange, yellow, green, blue, indigo or violet. Also, the following conditions should be satisfied:

  * Each of the seven colors should be used to paint at least one egg. 
  * Any four eggs lying sequentially should be painted different colors. 



Help the Easter Rabbit paint the eggs in the required manner. We know that it is always possible.

Input

The only line contains an integer n — the amount of eggs (7 ≤ n ≤ 100).

Output

Print one line consisting of n characters. The i-th character should describe the color of the i-th egg in the order they lie in the circle. The colors should be represented as follows: "R" stands for red, "O" stands for orange, "Y" stands for yellow, "G" stands for green, "B" stands for blue, "I" stands for indigo, "V" stands for violet.

If there are several answers, print any of them.

Examples

Input

8


Output

ROYGRBIV


Input

13


Output

ROYGBIVGBIVYG

Note

The way the eggs will be painted in the first sample is shown on the picture: 

<image>
"""

def paint_easter_eggs(n: int) -> str:
    """
    Paints n eggs in a circle with the following conditions:
    - Each of the seven colors (red, orange, yellow, green, blue, indigo, violet) should be used at least once.
    - Any four consecutive eggs should be painted different colors.

    Parameters:
    n (int): The number of eggs to paint (7 ≤ n ≤ 100).

    Returns:
    str: A string of length n representing the colors of the eggs.
    """
    s = 'ROYGBIV'
    s1 = 'GBIV'
    return s + (n - 7) // 4 * s1 + s1[:(n - 7) % 4]
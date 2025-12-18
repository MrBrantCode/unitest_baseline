"""
QUESTION:
Vanya got n cubes. He decided to build a pyramid from them. Vanya wants to build the pyramid as follows: the top level of the pyramid must consist of 1 cube, the second level must consist of 1 + 2 = 3 cubes, the third level must have 1 + 2 + 3 = 6 cubes, and so on. Thus, the i-th level of the pyramid must have 1 + 2 + ... + (i - 1) + i cubes.

Vanya wants to know what is the maximum height of the pyramid that he can make using the given cubes.


-----Input-----

The first line contains integer n (1 ≤ n ≤ 10^4) — the number of cubes given to Vanya.


-----Output-----

Print the maximum possible height of the pyramid in the single line.


-----Examples-----
Input
1

Output
1

Input
25

Output
4



-----Note-----

Illustration to the second sample:  [Image]
"""

def calculate_max_pyramid_height(n: int) -> int:
    """
    Calculate the maximum height of the pyramid that can be built with the given number of cubes.

    The pyramid is built such that:
    - The top level has 1 cube.
    - The second level has 1 + 2 = 3 cubes.
    - The third level has 1 + 2 + 3 = 6 cubes.
    - And so on...

    Args:
        n (int): The number of cubes given to Vanya.

    Returns:
        int: The maximum possible height of the pyramid.
    """
    cubes = 1
    last = 1
    stage = 0
    
    while n >= cubes:
        n -= cubes
        last += 1
        stage += 1
        cubes += last
    
    return stage
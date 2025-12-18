"""
QUESTION:
Emuskald needs a fence around his farm, but he is too lazy to build it himself. So he purchased a fence-building robot.

He wants the fence to be a regular polygon. The robot builds the fence along a single path, but it can only make fence corners at a single angle a.

Will the robot be able to build the fence Emuskald wants? In other words, is there a regular polygon which angles are equal to a?


-----Input-----

The first line of input contains an integer t (0 < t < 180) — the number of tests. Each of the following t lines contains a single integer a (0 < a < 180) — the angle the robot can make corners at measured in degrees.


-----Output-----

For each test, output on a single line "YES" (without quotes), if the robot can build a fence Emuskald wants, and "NO" (without quotes), if it is impossible.


-----Examples-----
Input
3
30
60
90

Output
NO
YES
YES



-----Note-----

In the first test case, it is impossible to build the fence, since there is no regular polygon with angle $30^{\circ}$.

In the second test case, the fence is a regular triangle, and in the last test case — a square.
"""

def can_build_regular_polygon(angle: int) -> str:
    """
    Determines if a robot can build a regular polygon with a given corner angle.

    Parameters:
    angle (int): The angle in degrees at which the robot can make corners.

    Returns:
    str: "YES" if the robot can build a regular polygon with the given angle, otherwise "NO".
    """
    n = 360 / (180 - angle)
    if n.is_integer():
        return "YES"
    else:
        return "NO"
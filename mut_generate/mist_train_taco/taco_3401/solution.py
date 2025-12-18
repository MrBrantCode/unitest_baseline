"""
QUESTION:
$\textit{ABC}$ is a right triangle, $90^{\circ}$ at $\mbox{B}$.

Therefore, $\angle ABC=90°$.

Point $\mbox{M}$ is the midpoint of hypotenuse $\mbox{AC}$.

You are given the lengths $\boldsymbol{AB}$ and $\mbox{BC}$. 

Your task is to find $\measuredangle MBC$  (angle $\theta^o$, as shown in the figure) in degrees.

Input Format

The first line contains the length of side $\boldsymbol{AB}$.

The second line contains the length of side $\mbox{BC}$.  

Constraints

$\textbf{0}<AB\leq100$
 
$\textbf{0}<BC\leq100$
Lengths $\boldsymbol{AB}$ and $\mbox{BC}$ are natural numbers.

Output Format

Output $\measuredangle MBC$ in degrees. 

Note: Round the angle to the nearest integer.

Examples: 

If angle is 56.5000001°, then output 57°. 

If angle is 56.5000000°, then output 57°. 

If angle is 56.4999999°, then output 56°.  

$0^\circ<\theta^\circ<90^\circ$

Sample Input
10
10

Sample Output
45°
"""

import math

def calculate_angle_MBC(ab: float, bc: float) -> int:
    """
    Calculate the angle MBC in a right triangle ABC where angle ABC is 90°.
    
    Parameters:
    ab (float): The length of side AB.
    bc (float): The length of side BC.
    
    Returns:
    int: The angle MBC in degrees, rounded to the nearest integer.
    """
    # Calculate the angle in radians using atan2
    angle_radians = math.atan2(ab, bc)
    
    # Convert the angle to degrees
    angle_degrees = math.degrees(angle_radians)
    
    # Round the angle to the nearest integer
    rounded_angle = round(angle_degrees)
    
    return rounded_angle
"""
QUESTION:
Polar coordinates are an alternative way of representing Cartesian coordinates or Complex Numbers.

A complex number $z$ 

$z=x+yj$
is completely determined by its real part $\boldsymbol{x}$ and imaginary part $y$. 

Here, $j$ is the imaginary unit.

A polar coordinate ($r,\varphi$)

is completely determined by modulus $\textbf{r}$ and phase angle $\mbox{p}$.

If we convert complex number $z$ to its polar coordinate, we find:

$\textbf{r}$: Distance from $z$ to origin, i.e., $\sqrt{x^2+y^2}$

$\mbox{p}$: Counter clockwise angle measured from the positive $\boldsymbol{x}$-axis to the line segment that joins $z$ to the origin.

Python's cmath module provides access to the mathematical functions for complex numbers.

$c\textit{math.phase}$ 

This tool returns the phase of complex number $z$ (also known as the argument of $z$).

>>> phase(complex(-1.0, 0.0))
3.1415926535897931

$\boldsymbol{abs}$ 

This tool returns the modulus (absolute value) of complex number $z$.

>>> abs(complex(-1.0, 0.0))
1.0

Task 

You are given a complex $z$. Your task is to convert it to polar coordinates.

Input Format

A single line containing the complex number $z$. 
 Note: complex() function can be used in python to convert the input as a complex number.

Constraints

Given number is a valid complex number

Output Format

Output two lines:

 The first line should contain the value of $\textbf{r}$.

 The second line should contain the value of $\mbox{p}$.

Sample Input
  1+2j

Sample Output
 2.23606797749979 
 1.1071487177940904

Note: The output should be correct up to 3 decimal places.
"""

import cmath

def convert_to_polar(z: str) -> tuple:
    """
    Converts a complex number to its polar coordinates.

    Parameters:
    z (str): A string representing a complex number.

    Returns:
    tuple: A tuple containing the modulus (r) and phase (p) of the complex number,
           both rounded to 3 decimal places.
    """
    # Convert the input string to a complex number
    complex_z = complex(z)
    
    # Calculate the modulus (r)
    r = abs(complex_z)
    
    # Calculate the phase (p)
    p = cmath.phase(complex_z)
    
    # Return the results rounded to 3 decimal places
    return round(r, 3), round(p, 3)
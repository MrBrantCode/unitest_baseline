"""
QUESTION:
You are given four points $A,B,C$ and $\mbox{D}$ in a 3-dimensional Cartesian coordinate system. You are required to print the angle between the plane made by the points $A,B,C$ and $B,C,D$ in degrees(not radians). Let the angle be $\textit{PHI}$. 

$\textit{Cos}(PHI)=(X.Y)/|X||Y|$ where $X=\textit{AB}$ x $\mbox{BC}$ and $\textbf{Y}=\textit{BC}$ x $\boldsymbol{\mathrm{CD}}$. 

Here, $X.Y$ means the dot product of $\mbox{X}$ and $\mathbf{Y}$, and $\boldsymbol{AB}$ x $\mbox{BC}$ means the cross product of vectors $\boldsymbol{AB}$ and $\mbox{BC}$. Also, $\textit{AB}=B-A$.

Input Format

One line of input containing the space separated floating number values of the $X,Y$ and $\mbox{z}$ coordinates of a point.  

Output Format

Output the angle correct up to two decimal places.

Sample Input

0 4 5
1 7 6
0 5 9
1 7 2

Sample Output

8.19
"""

from math import acos, degrees

def vector(a, b):
    return [b[0] - a[0], b[1] - a[1], b[2] - a[2]]

def length(a):
    return (a[0] ** 2 + a[1] ** 2 + a[2] ** 2) ** 0.5

def cross_product(a, b):
    c_x = a[1] * b[2] - a[2] * b[1]
    c_y = a[2] * b[0] - a[0] * b[2]
    c_z = a[0] * b[1] - a[1] * b[0]
    return [c_x, c_y, c_z]

def dot_product(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]

def angle_between(a, b):
    return acos(dot_product(a, b) / (length(a) * length(b)))

def calculate_angle_between_planes(a, b, c, d):
    ab = vector(a, b)
    bc = vector(b, c)
    cd = vector(c, d)
    x = cross_product(ab, bc)
    y = cross_product(bc, cd)
    angle_radians = angle_between(x, y)
    angle_degrees = degrees(angle_radians)
    return round(angle_degrees, 2)
"""
QUESTION:
The educational program (AHK Education) of the Aiz Broadcasting Association broadcasts a handicraft program for children, "Play with Tsukuro". This time I will make a box with sticks, but I would like to see if I can make a rectangular parallelepiped using the 12 sticks I prepared. However, the stick must not be cut or broken.




Given the lengths of the twelve bars, write a program to determine if you can create a rectangular parallelepiped with all of them as sides.



Input

The input is given in the following format.


e1 e2 ... e12


The input consists of one line and is given the integer ei (1 ≤ ei ≤ 100) representing the length of each bar.

Output

If a rectangular parallelepiped can be created, "yes" is output, and if it cannot be created, "no" is output. However, since a cube is a kind of rectangular parallelepiped, "yes" is output even if it is a cube.

Examples

Input

1 1 3 4 8 9 7 3 4 5 5 5


Output

no


Input

1 1 2 2 3 1 2 3 3 3 1 2


Output

yes
"""

def can_form_rectangular_parallelepiped(stick_lengths):
    # Ensure the input list has exactly 12 elements
    if len(stick_lengths) != 12:
        return "no"
    
    # Sort the list of stick lengths
    stick_lengths.sort()
    
    # Check if the sorted list can form a rectangular parallelepiped
    if (stick_lengths[0] == stick_lengths[1] == stick_lengths[2] == stick_lengths[3] and
        stick_lengths[4] == stick_lengths[5] == stick_lengths[6] == stick_lengths[7] and
        stick_lengths[8] == stick_lengths[9] == stick_lengths[10] == stick_lengths[11]):
        return "yes"
    else:
        return "no"
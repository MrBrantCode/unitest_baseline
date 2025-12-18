"""
QUESTION:
Create a program that rotates the pattern of 8 characters x 8 lines clockwise by 90 degrees, 180 degrees, and 270 degrees and outputs it.



Input

A pattern consisting of 8 characters x 8 lines is given. Characters consist of alphanumeric characters, half-width pound'#', and asterisk'*'.

Output

Output the rotated pattern in the following format.


90 (fixed half-width numbers)
Pattern rotated 90 degrees
180 (fixed half-width numbers)
180 degree rotated pattern
270 (fixed half-width numbers)
Pattern rotated 270 degrees


Examples

Input

#*******
#*******
#*******
#*******
#*******
#*******
#*******
########


Output

90
########
#*******
#*******
#*******
#*******
#*******
#*******
#*******
180
########
*******#
*******#
*******#
*******#
*******#
*******#
*******#
270
*******#
*******#
*******#
*******#
*******#
*******#
*******#
########


Input

*******
*******
*******
*******
*******
*******
*******


Output

90

*******
*******
*******
*******
*******
*******
*******
180

*******#
*******#
*******#
*******#
*******#
*******#
*******#
270
*******#
*******#
*******#
*******#
*******#
*******#
*******#
"""

def rotate_pattern(pattern):
    def rotate_90(matrix):
        return [list(row) for row in zip(*matrix[::-1])]

    def rotate_180(matrix):
        return rotate_90(rotate_90(matrix))

    def rotate_270(matrix):
        return rotate_90(rotate_180(matrix))

    rotated_patterns = {
        '90': rotate_90(pattern),
        '180': rotate_180(pattern),
        '270': rotate_270(pattern)
    }
    
    return rotated_patterns
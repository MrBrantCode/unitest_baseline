"""
QUESTION:
During the breaks between competitions, top-model Izabella tries to develop herself and not to be bored. For example, now she tries to solve Rubik's cube 2x2x2.

It's too hard to learn to solve Rubik's cube instantly, so she learns to understand if it's possible to solve the cube in some state using 90-degrees rotation of one face of the cube in any direction.

To check her answers she wants to use a program which will for some state of cube tell if it's possible to solve it using one rotation, described above.

Cube is called solved if for each face of cube all squares on it has the same color.

https://en.wikipedia.org/wiki/Rubik's_Cube


-----Input-----

In first line given a sequence of 24 integers a_{i} (1 ≤ a_{i} ≤ 6), where a_{i} denotes color of i-th square. There are exactly 4 occurrences of all colors in this sequence.


-----Output-----

Print «YES» (without quotes) if it's possible to solve cube using one rotation and «NO» (without quotes) otherwise.


-----Examples-----
Input
2 5 4 6 1 3 6 2 5 5 1 2 3 5 3 1 1 2 4 6 6 4 3 4

Output
NO
Input
5 3 5 3 2 5 2 5 6 2 6 2 4 4 4 4 1 1 1 1 6 3 6 3

Output
YES


-----Note-----

In first test case cube looks like this: [Image] 

In second test case cube looks like this:  [Image] 

It's possible to solve cube by rotating face with squares with numbers 13, 14, 15, 16.
"""

def can_solve_cube_with_one_rotation(cube_state):
    # Check if the cube can be solved with one rotation
    if (cube_state[2] == cube_state[4] == cube_state[22] == cube_state[24] and
        cube_state[1] == cube_state[3] == cube_state[6] == cube_state[8] and
        cube_state[13] == cube_state[14] == cube_state[15] == cube_state[16] and
        cube_state[17] == cube_state[18] == cube_state[19] == cube_state[20] and
        cube_state[21] == cube_state[23] == cube_state[9] == cube_state[11] and
        cube_state[5] == cube_state[7] == cube_state[10] == cube_state[12]):
        return "YES"
    
    elif (cube_state[13] == cube_state[14] == cube_state[15] == cube_state[16] and
          cube_state[17] == cube_state[18] == cube_state[19] == cube_state[20] and
          cube_state[2] == cube_state[4] == cube_state[5] == cube_state[7] and
          cube_state[6] == cube_state[8] == cube_state[9] == cube_state[11] and
          cube_state[10] == cube_state[12] == cube_state[22] == cube_state[24] and
          cube_state[1] == cube_state[3] == cube_state[21] == cube_state[23]):
        return "YES"
    
    elif (cube_state[1] == cube_state[2] == cube_state[3] == cube_state[4] and
          cube_state[9] == cube_state[10] == cube_state[11] == cube_state[12] and
          cube_state[13] == cube_state[14] == cube_state[23] == cube_state[24] and
          cube_state[5] == cube_state[6] == cube_state[15] == cube_state[16] and
          cube_state[17] == cube_state[18] == cube_state[7] == cube_state[8] and
          cube_state[21] == cube_state[22] == cube_state[19] == cube_state[20]):
        return "YES"
    
    elif (cube_state[1] == cube_state[2] == cube_state[3] == cube_state[4] and
          cube_state[9] == cube_state[10] == cube_state[11] == cube_state[12] and
          cube_state[13] == cube_state[14] == cube_state[7] == cube_state[8] and
          cube_state[5] == cube_state[6] == cube_state[19] == cube_state[20] and
          cube_state[17] == cube_state[18] == cube_state[23] == cube_state[24] and
          cube_state[21] == cube_state[22] == cube_state[15] == cube_state[16]):
        return "YES"
    
    elif (cube_state[5] == cube_state[6] == cube_state[7] == cube_state[8] and
          cube_state[21] == cube_state[22] == cube_state[23] == cube_state[24] and
          cube_state[3] == cube_state[4] == cube_state[13] == cube_state[15] and
          cube_state[14] == cube_state[16] == cube_state[11] == cube_state[12] and
          cube_state[9] == cube_state[10] == cube_state[18] == cube_state[20] and
          cube_state[17] == cube_state[19] == cube_state[1] == cube_state[2]):
        return "YES"
    
    elif (cube_state[5] == cube_state[6] == cube_state[7] == cube_state[8] and
          cube_state[21] == cube_state[22] == cube_state[23] == cube_state[24] and
          cube_state[3] == cube_state[4] == cube_state[18] == cube_state[20] and
          cube_state[14] == cube_state[16] == cube_state[1] == cube_state[2] and
          cube_state[9] == cube_state[10] == cube_state[13] == cube_state[15] and
          cube_state[17] == cube_state[19] == cube_state[11] == cube_state[12]):
        return "YES"
    
    else:
        return "NO"
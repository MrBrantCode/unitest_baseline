"""
QUESTION:
Artist Shinagawa was asked to exhibit n works. Therefore, I decided to exhibit the six sides of the cube colored with paint as a work. The work uses all six colors, Red, Yellow, Blue, Magenta, Green, and Cyan, and each side is filled with one color. Shinagawa changed the arrangement of colors even for cubic works with the same shape, and created n points as different works.

<image>



As a friend of mine, you, a friend of mine, allowed you to browse the work before exhibiting, and noticed that it was there. Even though they seemed to be colored differently, there were actually cubes with the same color combination. At this rate, it will not be possible to exhibit n works.

Please create a program that inputs the number of created works and the color information of each work and outputs how many more points you need to exhibit.

The color of each side of the cube is represented by the symbols from c1 to c6, and the arrangement is as follows. Also, each of c1 to c6 is one of Red, Yellow, Blue, Magenta, Green, and Cyan.

<image>




Input

A sequence of multiple datasets is given as input. The end of the input is indicated by a single line of zeros. Each dataset is given in the following format:


n
cube1
cube2
::
cuben


The first line gives the number of works n (1 ≤ n ≤ 30), and the following n lines give information on the i-th work. Information on each work is given in the following format.


c1 c2 c3 c4 c5 c6


The color arrangement ci of the work is given, separated by blanks.

The number of datasets does not exceed 100.

Output

For each dataset, output how many more works are needed to exhibit in one line.

Example

Input

3
Cyan Yellow Red Magenta Green Blue
Cyan Yellow Red Magenta Green Blue
Red Yellow Magenta Blue Green Cyan
4
Red Magenta Blue Green Yellow Cyan
Red Yellow Magenta Blue Green Cyan
Magenta Green Red Cyan Yellow Blue
Cyan Green Yellow Blue Magenta Red
0


Output

1
1
"""

def calculate_additional_works_needed(n, cubes):
    D = [(1, 5, 2, 3, 0, 4), (3, 1, 0, 5, 4, 2), (4, 0, 2, 3, 5, 1), (2, 1, 5, 0, 4, 3)]
    p_dice = (0, 0, 0, 1, 1, 2, 2, 3) * 3

    def rotate_dice(L0):
        L = L0[:]
        for k in p_dice:
            yield L
            L[:] = (L[e] for e in D[k])

    res = []
    for cube in cubes:
        cube_colors = cube.split()
        for dice in rotate_dice(cube_colors):
            if dice in res:
                break
        else:
            res.append(cube_colors)
    
    return n - len(res)
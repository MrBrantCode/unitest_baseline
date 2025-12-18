"""
QUESTION:
There is a cube which consists of n × n × n small cubes. Small cubes have marks on their surfaces. An example where n = 4 is shown in the following figure.


<image>


Then, as shown in the figure above (right), make a hole that penetrates horizontally or vertically from the marked surface to the opposite surface.

Your job is to create a program that reads the positions marked n and counts the number of small cubes with no holes.



Input

The input consists of several datasets. Each dataset is given in the following format:


n h
c1 a1 b1
c2 a2 b2
..
..
..
ch ah bh


h is an integer indicating the number of marks. The h lines that follow enter the positions of the h marks. The coordinate axes shown in the figure below will be used to specify the position of the mark. (x, y, z) = (1, 1, 1) is the lower left cube, and (x, y, z) = (n, n, n) is the upper right cube.


<image>


ci is a string indicating the plane marked with the i-th. ci is one of "xy", "xz", and "yz", indicating that the i-th mark is on the xy, xz, and yz planes, respectively.

ai and bi indicate the coordinates on the plane indicated by ci. For the xy, xz, and yz planes, ai and bi indicate the plane coordinates (x, y), (x, z), and (y, z), respectively. For example, in the above figure, the values ​​of ci, ai, and bi of marks A, B, and C are "xy 4 4", "xz 1 2", and "yz 2 3", respectively.

When both n and h are 0, it indicates the end of input.

You can assume that n ≤ 500 and h ≤ 200.

Output

For each dataset, print the number of non-perforated cubes on one line.

Example

Input

4 3
xy 4 4
xz 1 2
yz 2 3
4 5
xy 1 1
xy 3 3
xz 3 3
yz 2 1
yz 3 3
0 0


Output

52
46
"""

def count_non_perforated_cubes(n, h, marks):
    if n == 0:
        return 0
    
    perforated_cubes = set()
    
    for (ci, ai, bi) in marks:
        ai -= 1  # Adjusting to 0-based index
        bi -= 1  # Adjusting to 0-based index
        
        if ci == 'xy':
            for z in range(n):
                perforated_cubes.add(ai + (bi << 9) + (z << 18))
        elif ci == 'xz':
            for y in range(n):
                perforated_cubes.add(ai + (y << 9) + (bi << 18))
        elif ci == 'yz':
            for x in range(n):
                perforated_cubes.add(x + (ai << 9) + (bi << 18))
    
    total_cubes = n ** 3
    non_perforated_cubes = total_cubes - len(perforated_cubes)
    
    return non_perforated_cubes
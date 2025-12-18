"""
QUESTION:
There are n vertical lines in the Amidakuji. This Amidakuji meets the following conditions.

* Draw a horizontal line right next to it. Do not pull diagonally.
* Horizontal lines always connect adjacent vertical lines. In other words, the horizontal line does not cross the vertical line.
* For any vertical line, horizontal lines will not appear at the same time on the left and right from the same point. That is, the horizontal line does not cross the vertical line.
* There is only one hit.



The figure below shows an example of Amidakuji when n = 5. The numbers on the top represent the vertical line numbers (1, 2, 3, 4, 5 from the left). ☆ is a hit.

<image>


Create a program that reads the number of vertical lines n, the number m of the selected vertical line, the location of the Amidakuji hit, and the presence or absence of horizontal lines in each row, and outputs a judgment as to whether or not the hit can be reached. However, only one horizontal line can be added at any position in the given Amidakuji (it is not necessary to add it). The Amidakuji after adding one horizontal line must also meet the above conditions.



Input

Given multiple datasets. Each dataset is as follows:

The number of vertical lines n (1 <n ≤ 10) is written on the first line.
On the second line, the number m (1 ≤ m ≤ n) of the selected vertical line is written.
On the third line, the number of the hit place (☆ in the figure) is written counting from the left.
On the 4th line, the number of stages d (1 ≤ d ≤ 30) of Amidakuji is written.
From the 5th line onward, n-1 numbers are lined up in order from the top of the Amidakuji, with 1 being the horizontal line between each vertical line and 0 being the absence, as in the sequence of numbers corresponding to the figure. is.


The input ends on a line with a single 0.

Output

For each dataset, output the following values ​​depending on whether you can reach the hit from the selected vertical line number m.

* Output 0 if you can reach the hit without drawing a horizontal line.
* If you can reach the hit by drawing one horizontal line, output the position of the horizontal line closest to the starting side (upper in the figure). Please output the number of steps (see the figure) counting from the departure side and the number of vertical lines counting from the left to draw the horizontal line to the right, separated by a half-width space.
* If you cannot reach the hit even if you draw one horizontal line, output 1.

Example

Input

5
2
3
9
1010
1001
0100
1001
0010
1000
0100
0101
1010
0


Output

6 4
"""

def amidakuji_solver(n, m, p, d, horizontal_lines):
    m -= 1  # Convert to 0-based index
    p -= 1  # Convert to 0-based index
    
    # Initialize the state array
    s = [[0 for _ in range(n)] for _ in range(d + 1)]
    s[d] = [i for i in range(n)]
    
    # Fill the state array from bottom to top
    for i in range(d - 1, -1, -1):
        for j in range(n):
            s[i][j] = s[i + 1][j]
        for j in range(n - 1):
            if horizontal_lines[i][j]:
                s[i][j], s[i][j + 1] = s[i][j + 1], s[i][j]
    
    k = s[0][m]
    if k == p:
        return 0
    
    # Check if we can reach the hit by adding one horizontal line
    for i in range(d):
        for j in range(n - 1):
            if (s[i][j] == k and s[i][j + 1] == p or (s[i][j] == p and s[i][j + 1] == k)) and (j == 0 or horizontal_lines[i][j - 1] == 0) and (horizontal_lines[i][j] == 0) and (j == n - 2 or horizontal_lines[i][j + 1] == 0):
                return (i + 1, j + 1)  # Convert to 1-based index
    
    return 1
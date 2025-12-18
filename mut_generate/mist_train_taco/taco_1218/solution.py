"""
QUESTION:
Petya is the most responsible worker in the Research Institute. So he was asked to make a very important experiment: to melt the chocolate bar with a new laser device. The device consists of a rectangular field of n × m cells and a robotic arm. Each cell of the field is a 1 × 1 square. The robotic arm has two lasers pointed at the field perpendicularly to its surface. At any one time lasers are pointed at the centres of some two cells. Since the lasers are on the robotic hand, their movements are synchronized — if you move one of the lasers by a vector, another one moves by the same vector.

The following facts about the experiment are known: 

  * initially the whole field is covered with a chocolate bar of the size n × m, both lasers are located above the field and are active; 
  * the chocolate melts within one cell of the field at which the laser is pointed; 
  * all moves of the robotic arm should be parallel to the sides of the field, after each move the lasers should be pointed at the centres of some two cells; 
  * at any one time both lasers should be pointed at the field. Petya doesn't want to become a second Gordon Freeman. 



You are given n, m and the cells (x1, y1) and (x2, y2), where the lasers are initially pointed at (xi is a column number, yi is a row number). Rows are numbered from 1 to m from top to bottom and columns are numbered from 1 to n from left to right. You are to find the amount of cells of the field on which the chocolate can't be melted in the given conditions.

Input

The first line contains one integer number t (1 ≤ t ≤ 10000) — the number of test sets. Each of the following t lines describes one test set. Each line contains integer numbers n, m, x1, y1, x2, y2, separated by a space (2 ≤ n, m ≤ 109, 1 ≤ x1, x2 ≤ n, 1 ≤ y1, y2 ≤ m). Cells (x1, y1) and (x2, y2) are distinct.

Output

Each of the t lines of the output should contain the answer to the corresponding input test set.

Examples

Input

2
4 4 1 1 3 3
4 3 1 1 2 2


Output

8
2
"""

def calculate_unmelted_chocolate_cells(n, m, x1, y1, x2, y2):
    # Ensure x1 <= x2 and y1 <= y2
    if x1 > x2:
        x1, x2 = x2, x1
    if y1 > y2:
        y1, y2 = y2, y1
    
    # Calculate the dimensions of the overlapping area
    overlap_width = n - (x2 - x1)
    overlap_height = m - (y2 - y1)
    
    # Calculate the number of cells that can be melted by both lasers
    melted_cells = (overlap_width * overlap_height) * 2
    
    # Adjust for any excess width or height that doesn't fit within the field
    excess_width = max(0, (overlap_width * 2) - n)
    excess_height = max(0, (overlap_height * 2) - m)
    
    # Subtract the excess cells from the total melted cells
    melted_cells -= excess_width * excess_height
    
    # Total cells in the field
    total_cells = n * m
    
    # Calculate the number of unmelted cells
    unmelted_cells = total_cells - melted_cells
    
    return unmelted_cells
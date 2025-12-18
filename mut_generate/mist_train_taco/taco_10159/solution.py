"""
QUESTION:
Areas on the Cross-Section Diagram

Your task is to simulate a flood damage.

For a given cross-section diagram, reports areas of flooded sections.

<image>



Assume that rain is falling endlessly in the region and the water overflowing from the region is falling in the sea at the both sides. For example, for the above cross-section diagram, the rain will create floods which have areas of 4, 2, 1, 19 and 9 respectively.

output

Report the areas of floods in the following format:

$A$
$k$ $L_1$ $L_2$ ... $L_k$

In the first line, print the total area $A$ of created floods.

In the second line, print the number of floods $k$ and areas $L_i (i = 1, 2, ..., k)$ for each flood from the left side of the cross-section diagram. Print a space character before $L_i$.

Constraints

* $1 \leq$ length of the string $\leq 20,000$

Input

A string, which represents slopes and flatlands by '/', '\' and '_' respectively, is given in a line. For example, the region of the above example is given by a string "\\\///\\_/\/\\\\\\\/_/\\\///__\\\\\\_\\\/_\/_/\".

Examples

Input

\\//


Output

4
1 4


Input

\\///\_/\/\\\\/_/\\///__\\\_\\/_\/_/\


Output

35
5 4 2 1 19 9
"""

def calculate_flood_areas(cross_section: str) -> tuple[int, list[int]]:
    down = []
    edge = []
    pool = []
    
    for i, c in enumerate(cross_section):
        if c == '\\':
            down.append(i)
        elif c == '/' and down:
            left = down.pop()
            area = i - left
            while edge:
                if edge[-1] < left:
                    break
                edge.pop()
                area += pool.pop()
            edge.append(left)
            pool.append(area)
    
    total_area = sum(pool)
    flood_areas = pool
    
    return total_area, flood_areas
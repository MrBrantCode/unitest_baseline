"""
QUESTION:
Galileo's latest project involves determining the density of stars in certain regions of the sky. For this purpose he started looking for datasets online, and discovered a dataset on Newton's blog. Newton had decomposed the night sky into a Voronoi tessellation with the generators arranged in a grid. He has stored the number of stars in a Voronoi cell at a position in a matrix that corresponds to the position of the generator in the grid.
This dataset does not directly help Galileo, because he needs to be able to query the number of stars in a rectangular portion of the sky. Galileo tried to write a program that does this on his own, but it turned out to be too slow. Can you help him?

-----Input Format-----
The first line contains two integers n and m that denote the height and width of the matrix respectively. This is followed by  n lines each containing m integers each.
The line following this would contain a single integer t, the number of queries to be run. Each query line consists of 4 integers px, py, qx, qy. The first two integers denote the row and column numbers of the upper left corner of the rectangular region, and the second pair of numbers correspond to the lower right corner.

-----Output Format-----
For each query output a single line containing the number of stars in that rectangular region.

-----Example-----
Input:

3 3
10 10 10
10 10 10
10 10 10
4
1 1 1 1
1 1 3 3
2 1 3 3
3 1 3 3

Output:

10
90
60
30
"""

def query_stars_in_rectangular_regions(matrix, queries):
    """
    Calculate the number of stars in specified rectangular regions of a Voronoi tessellation matrix.

    Parameters:
    - matrix (list of list of int): A 2D list where each element represents the number of stars in a Voronoi cell.
    - queries (list of tuple): A list of tuples, each containing four integers (px, py, qx, qy) representing the 
      coordinates of the upper left and lower right corners of the rectangular region to query.

    Returns:
    - list of int: A list where each element is the number of stars in the corresponding rectangular region.
    """
    results = []
    for (px, py, qx, qy) in queries:
        total_stars = 0
        for i in range(px - 1, qx):
            for j in range(py - 1, qy):
                total_stars += matrix[i][j]
        results.append(total_stars)
    return results
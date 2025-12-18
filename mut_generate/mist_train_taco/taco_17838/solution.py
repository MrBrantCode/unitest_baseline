"""
QUESTION:
K: Relief (Angel Relief)

Tenma, an angel, decides to save a city.

The city has a rectangular shape divided into north-south $ H $ parcels x east-west $ W $ parcels, with houses in each parcel.

The $ X $ th section from the north and the $ Y $ th section from the west are represented by $ (X, Y) $.

The house in parcel $ (i, j) $ is inhabited by $ A_ {i, j} $ people.

Tenshin chooses a rectangular area whose sides are parallel or vertical to north-south or east-west, and rescues all the people living in it one by one.

Tenshin does this for every possible rectangle.

Find the total number of times Tenma-san rescues people.

input

The integers $ H, W $ are given on the first line, separated by blanks.

Of the following $ H $ lines, the integers $ A_ {i, 1}, A_ {i, 2}, A_ {i, 3}, \ dots, A_ {i, W} $ are blank on the $ i $ line. Given as a delimiter.

output

Output the total number of times Tenma-san rescues people.

Constraint

* $ H, W $ are integers between $ 1 $ and $ 500 $
* $ A_ {i, j} $ are all integers greater than or equal to $ 1 $ and less than or equal to $ 9 $.



Input example 1


twenty two
1 2
4 8


Output example 1


60


For example, if you choose a rectangular area with $ (1, 1) $ in the upper left and $ (2, 2) $ in the lower right, you will rescue $ 15 $ people there one by one, so a total of $ 15 $ times. Relief.

$ 1, 2, 3, 4, 5, 8, 10, 12, 15 $ relief for each of the $ 9 $ rectangular areas, for a total of $ 60 $.

Input example 2


twenty three
one two Three
4 5 6


Output example 2


140






Example

Input

2 2
1 2
4 8


Output

60
"""

def calculate_total_rescues(H, W, A):
    """
    Calculate the total number of times Tenma rescues people in the city.

    Parameters:
    H (int): The number of rows in the city grid.
    W (int): The number of columns in the city grid.
    A (list of lists): A 2D list representing the number of people in each parcel of the city.

    Returns:
    int: The total number of times Tenma rescues people.
    """
    total_rescues = 0
    for y in range(H):
        for x in range(W):
            total_rescues += (x + 1) * (W - x) * A[y][x] * (y + 1) * (H - y)
    return total_rescues
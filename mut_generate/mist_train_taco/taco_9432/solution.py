"""
QUESTION:
There are 2000001 stones placed on a number line. The coordinates of these stones are -1000000, -999999, -999998, \ldots, 999999, 1000000.
Among them, some K consecutive stones are painted black, and the others are painted white.
Additionally, we know that the stone at coordinate X is painted black.
Print all coordinates that potentially contain a stone painted black, in ascending order.

-----Constraints-----
 - 1 \leq K \leq 100
 - 0 \leq X \leq 100
 - All values in input are integers.

-----Input-----
Input is given from Standard Input in the following format:
K X

-----Output-----
Print all coordinates that potentially contain a stone painted black, in ascending order, with spaces in between.

-----Sample Input-----
3 7

-----Sample Output-----
5 6 7 8 9

We know that there are three stones painted black, and the stone at coordinate 7 is painted black. There are three possible cases:
 - The three stones painted black are placed at coordinates 5, 6, and 7.
 - The three stones painted black are placed at coordinates 6, 7, and 8.
 - The three stones painted black are placed at coordinates 7, 8, and 9.
Thus, five coordinates potentially contain a stone painted black: 5, 6, 7, 8, and 9.
"""

def find_black_stone_coordinates(K, X):
    # Calculate the leftmost and rightmost coordinates of the black stones
    leftmost = max(-1000000, X - (K - 1))
    rightmost = min(1000000, X + (K - 1))
    
    # Generate the list of coordinates from leftmost to rightmost
    black_stone_coordinates = list(range(leftmost, rightmost + 1))
    
    return black_stone_coordinates
"""
QUESTION:
Many computer strategy games require building cities, recruiting army, conquering tribes, collecting resources. Sometimes it leads to interesting problems. 

Let's suppose that your task is to build a square city. The world map uses the Cartesian coordinates. The sides of the city should be parallel to coordinate axes. The map contains mines with valuable resources, located at some points with integer coordinates. The sizes of mines are relatively small, i.e. they can be treated as points. The city should be built in such a way that all the mines are inside or on the border of the city square. 

Building a city takes large amount of money depending on the size of the city, so you have to build the city with the minimum area. Given the positions of the mines find the minimum possible area of the city.


-----Input-----

The first line of the input contains number n — the number of mines on the map (2 ≤ n ≤ 1000). Each of the next n lines contains a pair of integers x_{i} and y_{i} — the coordinates of the corresponding mine ( - 10^9 ≤ x_{i}, y_{i} ≤ 10^9). All points are pairwise distinct.


-----Output-----

Print the minimum area of the city that can cover all the mines with valuable resources.


-----Examples-----
Input
2
0 0
2 2

Output
4

Input
2
0 0
0 3

Output
9
"""

def calculate_minimum_city_area(mines):
    if not mines:
        return 0
    
    x_coords = [mine[0] for mine in mines]
    y_coords = [mine[1] for mine in mines]
    
    max_x = max(x_coords)
    min_x = min(x_coords)
    max_y = max(y_coords)
    min_y = min(y_coords)
    
    side_length = max(max_x - min_x, max_y - min_y)
    
    return side_length ** 2
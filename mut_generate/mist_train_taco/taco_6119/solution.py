"""
QUESTION:
Pavel made a photo of his favourite stars in the sky. His camera takes a photo of all points of the sky that belong to some rectangle with sides parallel to the coordinate axes.

Strictly speaking, it makes a photo of all points with coordinates $(x, y)$, such that $x_1 \leq x \leq x_2$ and $y_1 \leq y \leq y_2$, where $(x_1, y_1)$ and $(x_2, y_2)$ are coordinates of the left bottom and the right top corners of the rectangle being photographed. The area of this rectangle can be zero.

After taking the photo, Pavel wrote down coordinates of $n$ of his favourite stars which appeared in the photo. These points are not necessarily distinct, there can be multiple stars in the same point of the sky.

Pavel has lost his camera recently and wants to buy a similar one. Specifically, he wants to know the dimensions of the photo he took earlier. Unfortunately, the photo is also lost. His notes are also of not much help; numbers are written in random order all over his notepad, so it's impossible to tell which numbers specify coordinates of which points.

Pavel asked you to help him to determine what are the possible dimensions of the photo according to his notes. As there are multiple possible answers, find the dimensions with the minimal possible area of the rectangle.


-----Input-----

The first line of the input contains an only integer $n$ ($1 \leq n \leq 100\,000$), the number of points in Pavel's records.

The second line contains $2 \cdot n$ integers $a_1$, $a_2$, ..., $a_{2 \cdot n}$ ($1 \leq a_i \leq 10^9$), coordinates, written by Pavel in some order.


-----Output-----

Print the only integer, the minimal area of the rectangle which could have contained all points from Pavel's records.


-----Examples-----
Input
4
4 1 3 2 3 2 1 3

Output
1
Input
3
5 8 5 5 7 5

Output
0


-----Note-----

In the first sample stars in Pavel's records can be $(1, 3)$, $(1, 3)$, $(2, 3)$, $(2, 4)$. In this case, the minimal area of the rectangle, which contains all these points is $1$ (rectangle with corners at $(1, 3)$ and $(2, 4)$).
"""

def calculate_minimal_rectangle_area(n, coordinates):
    # Sort the coordinates
    coordinates.sort()
    
    # Extract the minimum and maximum x and y coordinates
    mix = coordinates[0]
    maxx = coordinates[n - 1]
    miy = coordinates[n]
    may = coordinates[-1]
    
    # Initialize the dynamic programming list with the first possible rectangle
    dp = []
    dp.append([maxx, mix, may, miy])
    
    # Generate all possible rectangles
    for i in range(1, n):
        dp.append([coordinates[-1], coordinates[0], coordinates[i + n - 1], coordinates[i]])
    
    # Calculate the minimal area
    ans = (dp[0][0] - dp[0][1]) * (dp[0][2] - dp[0][3])
    for i in dp:
        ans = min(ans, (i[0] - i[1]) * (i[2] - i[3]))
    
    return ans
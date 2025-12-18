"""
QUESTION:
problem

JOI City will hold a large-scale exposition.

There are two themes for this exposition, and each of the N exhibition facilities in JOI City will exhibit on one of the two themes.

The location of the facility is represented by plane coordinates (x, y). To move from the facility at position (x, y) to the facility at (x ′, y ′), | x − x ′ | + It takes only | y − y ′ | (for the integer a, | a | represents the absolute value of a). To create a sense of unity within the same theme, and to be interested in only one theme. In order not to make people feel inconvenience, I would like to assign the theme so that the travel time between two facilities exhibiting on the same theme is as short as possible. Unless the same theme is assigned to all exhibition facilities. , How can you divide the theme.

Let M be the maximum travel time between two facilities exhibiting on the same theme. Create a program to find the minimum value of M given the locations of N exhibition facilities.

output

The output consists of only one line. Output the maximum value M of the maximum travel time between two facilities exhibiting on the same theme.

Input / output example

Input example 1


Five
0 0
Ten
-1 -2
0 1
-1 1

Output example 1


3

In this case, for example, one theme for the facility at coordinates (0, 0), (1, 0), (0, 1), and another theme for the facility at (−1, −2), (−1, 1). When one theme is assigned, the travel time between two facilities exhibiting on the same theme is all 3 or less. Since the travel time cannot be all 2 or less, 3 is output.

The above question sentences and the data used for the automatic referee are the question sentences created and published by the Japan Committee for Information Olympics and the test data for scoring.



input

The first line of input contains the number of facilities N (3 ≤ N ≤ 100000 = 105). The first line of input i + 1 (1 ≤ i ≤ N) represents the coordinates of each facility. The two integers xi, yi (| xi | ≤ 100000 = 105, | yi | ≤ 100000 = 105) are separated by blanks. This is where the coordinates of the i-th facility are (xi, yi). It means that there can be no more than one facility at the same coordinates.

Of the scoring data, 40% of the points are N ≤ 2000.

Example

Input

5
0 0
1 0
-1 -2
0 1
-1 1


Output

3
"""

def find_min_max_travel_time(facilities):
    x = []
    y = []
    
    for (a, b) in facilities:
        x.append(a + b)
        y.append(a - b)
    
    xmin, xmax = min(x), max(x)
    ymin, ymax = min(y), max(y)
    
    ans1 = ans2 = 0
    
    for i in range(len(facilities)):
        d1 = max(x[i] - xmin, y[i] - ymin)
        d2 = max(xmax - x[i], ymax - y[i])
        ans1 = max(ans1, min(d1, d2))
        
        d1 = max(x[i] - xmin, ymax - y[i])
        d2 = max(xmax - x[i], y[i] - ymin)
        ans2 = max(ans2, min(d1, d2))
    
    return min(ans1, ans2)
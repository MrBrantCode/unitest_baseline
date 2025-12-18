"""
QUESTION:
Koto Municipal Subway

Koto Municipal Subway

Koto City is a famous city whose roads are in a grid pattern, as shown in the figure below. The roads extending from north to south and the roads extending from east to west are lined up at intervals of 1 km each. Let Koto station at the southwestern intersection of Koto city be (0, 0), and mark x km east and y km north from it as (x, y) (0 ≤ x, y). ).

<image>

In anticipation of an increase in tourists due to the Olympic Games to be held five years later, the city has decided to build a new subway line starting from Koto station. Currently, we are planning to lay a rail to Shin-Koto station, which will be newly constructed as the next station after Koto station. The rail will be laid straight from Koto station to Shin-Koto station. Therefore, when the location of Shin-Koto station is (x, y), the length of the rail is √ (x2 + y2). The cost of laying the rail is the same as the length of the laid rail. Even if the rail length is a decimal number such as 1.5km, the cost is also 1.5.

The location (x, y) of Shin-Koto station has not been decided yet, and we plan to make it a location that meets the following conditions.

* It is an intersection. That is, x and y are integers, respectively.
* The shortest distance walked along the road from Koto station is exactly D. That is, x + y = D is satisfied.



Among the above two conditions, select the location of Shin-Koto station so that the difference between the rail budget E and the rail cost set by the city | √ (x2 + y2) --E | is minimized. Here, | A | represents the absolute value of A. Your job is to create a program that outputs the difference between the cost and budget for laying rails when the Shin-Koto station was constructed as described above.

Input

The input consists of multiple data sets, and the number of data sets contained in one input is 100 or less. The format of each data set is as follows.

> D E

D (1 ≤ D ≤ 100) is an integer that represents the shortest distance when walking along the road from Koto station to Shin-Koto station. E (1 ≤ E ≤ 100) is an integer representing the budget for rail construction.

The end of the input is indicated by a line of two zeros separated by a blank.

Output

For each data set, output the difference between the cost and budget when laying the rail so as to satisfy the problem condition in one line. The answer must have an absolute error greater than 10-3. Note that if you do not output a line break at the end of each line, or if you output unnecessary characters, it will be judged as an incorrect answer.

Sample Input


twenty one
7 5
7 6
7 7
76 5
8 41
0 0

Output for Sample Input


0.4142135624
0
0.0827625303
0
48.7401153702
33

Hint

In the first data set, as shown in the figure below, an intersection 2 km along the road from Koto station is a candidate for a place to build Shin-Koto station.

<image>

When Shin-Koto station is constructed at each intersection, the difference between the cost for laying the rail and budget 1 is as follows.

* (2, 0): | √ (22 + 02) --1 | = 1.0
* (1, 1): | √ (12 + 12) --1 | = 0.4142135623 ...
* (0, 2): | √ (02 + 22) --1 | = 1.0



Therefore, the difference between the cost and the budget is minimized when the construction is done in (1, 1).





Example

Input

2 1
7 5
7 6
7 7
76 5
8 41
0 0


Output

0.4142135624
0
0.0827625303
0
48.7401153702
33
"""

import math

def calculate_min_rail_cost_difference(d: int, e: int) -> float:
    if d == 0 and e == 0:
        return 0.0
    
    x = d
    y = 0
    min_difference = abs(d - e)
    
    while y != d:
        rail_length = math.sqrt(x ** 2 + y ** 2)
        current_difference = abs(rail_length - e)
        min_difference = min(min_difference, current_difference)
        x -= 1
        y += 1
    
    return min_difference
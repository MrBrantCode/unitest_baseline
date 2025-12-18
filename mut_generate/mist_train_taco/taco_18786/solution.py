"""
QUESTION:
In 20XX, the Aizu Chuo Road, which has a total distance of 58km and 6 sections from Atsushiokanomachi, Kitakata City to Minamiaizucho, is scheduled to be completed and opened.

For half a year after opening, the toll will be halved for vehicles that pass the departure IC or arrival IC between 17:30 and 19:30 and have a mileage of 40km or less. However, the charge will be in units of 50 yen and rounded up. The table below is a list of fares and distances.

<image>

<image>


For example, from Kitakata (2) to Aizuwakamatsu (4), the fare is 450 yen and the distance is 12km. If it is half price time zone, it will be 250 yen.

Create a program that calculates and outputs the charge by inputting the departure IC, departure IC transit time, arrival IC, and arrival IC transit time. However, the time entered will be the value in 24-hour notation. In addition, even if you pass at exactly 17:30 and 19:30, it will be included in the half price time zone.



Input

A sequence of multiple datasets is given as input. The end of the input is indicated by a single line of zeros. Each dataset is given in the following format:


d
hd md
a
ha ma


The first line gives the departure IC number d (1 ≤ d ≤ 7), and the second line gives the time hd (0 ≤ hd ≤ 23) and minutes md (0 ≤ md ≤ 59) of the departure IC transit time. ..

The arrival IC number a (1 ≤ a ≤ 7) is given on the third line, and the time ha (0 ≤ ha ≤ 23) and minute ma (0 ≤ ma ≤ 59) of the arrival IC transit time are given on the fourth line. ..

Output

The toll (integer) is output to one line for each data set.

Example

Input

2
17 25
4
17 45
4
17 25
7
19 35
0


Output

250
1300
"""

import math

# Fare and distance matrix
M = [
    [0, 300, 500, 600, 700, 1350, 1650],
    [6, 0, 350, 450, 600, 1150, 1500],
    [13, 7, 0, 250, 400, 1000, 1350],
    [18, 12, 5, 0, 250, 850, 1300],
    [23, 17, 10, 5, 0, 600, 1150],
    [43, 37, 30, 25, 20, 0, 500],
    [58, 52, 45, 40, 35, 15, 0]
]

def intime(t):
    return 1730 <= t <= 1930

def getinfo(src, dst):
    if src > dst:
        (src, dst) = (dst, src)
    return (M[dst][src], M[src][dst])

def calculate_toll(departure_ic, departure_time, arrival_ic, arrival_time):
    # Convert time to a single integer for easy comparison
    t1 = 100 * departure_time[0] + departure_time[1]
    t2 = 100 * arrival_time[0] + arrival_time[1]
    
    # Get fare and distance information
    (a, b) = getinfo(departure_ic - 1, arrival_ic - 1)
    
    # Check if the time falls within the half price time zone and adjust the fare accordingly
    if (intime(t1) or intime(t2)) and a <= 40:
        b = (b // 2 + 49) // 50 * 50
    
    return b
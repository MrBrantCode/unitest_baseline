"""
QUESTION:
The New Vasjuki village is stretched along the motorway and that's why every house on it is characterized by its shift relative to some fixed point — the xi coordinate. The village consists of n houses, the i-th house is located in the point with coordinates of xi.

TELE3, a cellular communication provider planned to locate three base stations so as to provide every house in the village with cellular communication. The base station having power d located in the point t provides with communication all the houses on the segment [t - d, t + d] (including boundaries).

To simplify the integration (and simply not to mix anything up) all the three stations are planned to possess the equal power of d. Which minimal value of d is enough to provide all the houses in the village with cellular communication.

Input

The first line contains an integer n (1 ≤ n ≤ 2·105) which represents the number of houses in the village. The second line contains the coordinates of houses — the sequence x1, x2, ..., xn of integer numbers (1 ≤ xi ≤ 109). It is possible that two or more houses are located on one point. The coordinates are given in a arbitrary order.

Output

Print the required minimal power d. In the second line print three numbers — the possible coordinates of the base stations' location. Print the coordinates with 6 digits after the decimal point. The positions of the stations can be any from 0 to 2·109 inclusively. It is accepted for the base stations to have matching coordinates. If there are many solutions, print any of them.

Examples

Input

4
1 2 3 4


Output

0.500000
1.500000 2.500000 3.500000


Input

3
10 20 30


Output

0
10.000000 20.000000 30.000000


Input

5
10003 10004 10001 10002 1


Output

0.500000
1.000000 10001.500000 10003.500000
"""

def calculate_minimal_station_power(n, houses):
    houses = sorted(set(houses))
    
    if len(houses) <= 3:
        minimal_power = 0
        result = houses[:]
        while len(result) < 3:
            result.append(result[-1])
        station_locations = tuple(result)
        return minimal_power, station_locations
    
    span = 0
    left = 1
    right = len(houses) - 2
    
    while houses[right] - houses[left] > span:
        left_gap = houses[left] - houses[0] - span
        right_gap = houses[-1] - houses[right] - span
        middle = houses[right] - houses[left]
        
        if left_gap <= right_gap:
            if span + left_gap > middle:
                span = middle
                break
            left += 1
            if left_gap == right_gap:
                right -= 1
            span += left_gap
        else:
            if span + right_gap > middle:
                span = middle
                break
            right -= 1
            span += right_gap
    
    minimal_power = span / 2
    station_locations = (
        (houses[0] + houses[left - 1]) / 2,
        (houses[left] + houses[right]) / 2,
        (houses[right + 1] + houses[-1]) / 2
    )
    
    return minimal_power, station_locations
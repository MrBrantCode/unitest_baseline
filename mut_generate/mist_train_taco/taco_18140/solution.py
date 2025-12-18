"""
QUESTION:
Everybody knows that the capital of Bergeria is connected to banson by a direct road. To improve the road's traffic capacity, there was placed just one traffic sign, limiting the maximum speed. Traffic signs in Bergeria are a bit peculiar, because they limit the speed only at that point on the road where they are placed. Right after passing the sign it is allowed to drive at any speed.

It is known that the car of an average Bergeria citizen has the acceleration (deceleration) speed of a km/h2, and has maximum speed of v km/h. The road has the length of l km, and the speed sign, limiting the speed to w km/h, is placed d km (1 ≤ d < l) away from the capital of Bergeria. The car has a zero speed at the beginning of the journey. Find the minimum time that an average Bergeria citizen will need to get from the capital to banson, if he drives at the optimal speed.

The car can enter banson at any speed.

Input
The first line of the input file contains two integer numbers a and v (1 ≤ a, v ≤ 10000). The second line contains three integer numbers l, d and w (2 ≤ l ≤ 10000; 1 ≤ d < l; 1 ≤ w ≤ 10000).

Output
Print the answer with at least five digits after the decimal point.

SAMPLE INPUT
1 1
2 1 3

SAMPLE OUTPUT
2.500000000000
"""

def calculate_minimum_time(a: float, v: float, l: float, d: float, w: float) -> float:
    if v <= w or w * w >= 2 * a * d:
        if v * v <= 2 * a * l:
            return v / 2 / a + l / v
        else:
            return (2 * l / a) ** .5
    else:
        if v * v - w * w >= (l - d) * 2 * a:
            t = ((w * w + 2 * a * (l - d)) ** .5 - w) / a
        else:
            t = (l - d - (v * v - w * w) / 2 / a) / v + (v - w) / a
        if 2 * v * v - w * w >= 2 * a * d:
            t += (2 * (a * d + w * w / 2) ** .5 - w) / a
        else:
            t += (d - (2 * v * v - w * w) / 2 / a) / v + (2 * v - w) / a
        return t
"""
QUESTION:
Everybody knows that the capital of Berland is connected to Bercouver (the Olympic capital) by a direct road. To improve the road's traffic capacity, there was placed just one traffic sign, limiting the maximum speed. Traffic signs in Berland are a bit peculiar, because they limit the speed only at that point on the road where they are placed. Right after passing the sign it is allowed to drive at any speed.

It is known that the car of an average Berland citizen has the acceleration (deceleration) speed of a km/h2, and has maximum speed of v km/h. The road has the length of l km, and the speed sign, limiting the speed to w km/h, is placed d km (1 ≤ d < l) away from the capital of Berland. The car has a zero speed at the beginning of the journey. Find the minimum time that an average Berland citizen will need to get from the capital to Bercouver, if he drives at the optimal speed.

The car can enter Bercouver at any speed.

Input

The first line of the input file contains two integer numbers a and v (1 ≤ a, v ≤ 10000). The second line contains three integer numbers l, d and w (2 ≤ l ≤ 10000; 1 ≤ d < l; 1 ≤ w ≤ 10000).

Output

Print the answer with at least five digits after the decimal point.

Examples

Input

1 1
2 1 3


Output

2.500000000000


Input

5 70
200 170 40


Output

8.965874696353
"""

def calculate_minimum_time(a, v, l, d, w):
    def time_distance(v0, a, d):
        return (-v0 + (v0 ** 2 + 2 * a * d) ** 0.5) / a

    def time_accelerating(v0, v1, a):
        return (v1 - v0) / a

    def time_speed(v, d):
        return d / v

    def distance_travelled(v0, t, a):
        return v0 * t + a / 2 * t ** 2

    time = 0
    time_to_d = time_distance(0, a, d)
    time_to_v = time_accelerating(0, v, a)
    
    if (v if time_to_v <= time_to_d else time_to_d * a) <= w:
        acceleration_time = time_to_v
        acceleration_distance = distance_travelled(0, acceleration_time, a)
        if acceleration_distance >= l:
            time = time_distance(0, a, l)
        else:
            time = acceleration_time
            time += time_speed(v, l - acceleration_distance)
    else:
        if time_to_v <= time_to_d:
            acceleration_time = time_to_v
            acceleration_distance = distance_travelled(0, acceleration_time, a)
            deceleration_time = time_accelerating(v, w, -a)
            deceleration_distance = distance_travelled(v, deceleration_time, -a)
        if time_to_v > time_to_d or acceleration_distance + deceleration_distance > d:
            acceleration_time = time_accelerating(0, w, a)
            acceleration_distance = distance_travelled(0, acceleration_time, a)
            remaining_distance = d - acceleration_distance
            delta_time = time_distance(w, a, remaining_distance / 2)
            time = acceleration_time + 2 * delta_time
        else:
            time = time_to_v
            time += time_speed(v, d - deceleration_distance - acceleration_distance)
            time += deceleration_time
        acceleration_time = time_accelerating(w, v, a)
        acceleration_distance = distance_travelled(w, acceleration_time, a)
        if acceleration_distance >= l - d:
            time += time_distance(w, a, l - d)
        else:
            time += acceleration_time
            time += time_speed(v, l - (d + acceleration_distance))
    
    return round(time, 5)
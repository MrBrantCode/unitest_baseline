"""
QUESTION:
In 40XX, the Earth was invaded by aliens! Already most of the Earth has been dominated by aliens, leaving Tsuruga Castle Fortress as the only remaining defense base. Suppression units are approaching the Tsuruga Castle Fortress one after another.

<image>


But hope remains. The ultimate defense force weapon, the ultra-long-range penetrating laser cannon, has been completed. The downside is that it takes a certain distance to reach its power, and enemies that are too close can just pass through. Enemies who have invaded the area where power does not come out have no choice but to do something with other forces. The Defense Forces staff must know the number to deal with the invading UFOs, but it is unlikely to be counted well because there are too many enemies. So the staff ordered you to have a program that would output the number of UFOs that weren't shot down by the laser. Create a program by the time the battle begins and help protect the Tsuruga Castle Fortress.

Enemy UFOs just rush straight toward the base of the laser cannon (the UFOs are treated to slip through each other and do not collide). The laser cannon begins firing at the center of the nearest UFO one minute after the initial state, and then continues firing the laser every minute under the same conditions. The laser penetrates, and the UFO beyond it can be shot down with the laser just scratching it. However, this laser has a range where it is not powerful, and it is meaningless to aim a UFO that has fallen into that range, so it is designed not to aim. How many UFOs invaded the area where the power of the laser did not come out when it was shot down as much as possible?

Create a program that inputs the radius R of the range where the power of the laser does not come out and the information of the invading UFO, and outputs how many UFOs are invading without being shot down. The information on the incoming UFO consists of the number of UFOs N, the initial coordinates of each UFO (x0, y0), the radius r of each UFO, and the speed v of each UFO.

The origin of the coordinates (0, 0) is the position of the laser cannon. The distance between the laser cannon and the UFO is given by the distance from the origin to the center of the UFO, and UFOs with this distance less than or equal to R are within the range where the power of the laser does not come out. Consider that there are no cases where there are multiple targets to be aimed at at the same time. All calculations are considered on a plane and all inputs are given as integers.



Input

A sequence of multiple datasets is given as input. The end of the input is indicated by two lines of zeros. Each dataset is given in the following format:


R N
x01 y01 r1 v1
x02 y02 r2 v2
::
x0N y0N rN vN


The first line gives the radius R (1 ≤ R ≤ 500) and the number of UFOs N (1 ≤ N ≤ 100) within the range of laser power. The following N lines give the i-th UFO information x0i, y0i (-100 ≤ x0i, y0i ≤ 1000), ri, vi (1 ≤ ri, vi ≤ 500).

The number of datasets does not exceed 50.

Output

For each input dataset, it prints the number of UFOs that have invaded the area where the laser power does not come out on one line.

Example

Input

100 5
101 101 5 5
110 110 2 3
-112 -100 9 11
-208 160 82 90
-110 108 10 2
10 11
15 0 5 1
25 0 5 1
35 0 5 1
45 0 5 1
55 0 5 1
65 0 5 1
75 0 5 1
85 0 5 1
95 0 5 1
-20 0 5 20
-30 0 500 5
0 0


Output

1
1
"""

import math

class Ufo:
    def __init__(self, x, y, r, v):
        self.dist = get_dist(x, y)
        self.angle = get_angle(y, x)
        self.rad = r
        self.v = v

def get_dist(x, y):
    return (x ** 2 + y ** 2) ** (1 / 2)

def get_angle(x, y):
    angle = math.atan2(y, x)
    if angle < 0:
        angle += math.pi * 2
    return angle

def reache(ufos, R):
    remove_lst = []
    for (i, ufo) in enumerate(ufos):
        ufo.dist -= ufo.v
        if ufo.dist <= R:
            remove_lst.append(i)
    for i in reversed(remove_lst):
        ufos.pop(i)
    return len(remove_lst)

def is_dead(ufo, laser, R):
    diff = abs(ufo.angle - laser)
    if diff > math.pi:
        diff = math.pi * 2 - diff
    if diff <= math.pi / 2 and ufo.dist * math.sin(diff) <= ufo.rad or ufo.dist <= ufo.rad:
        if ufo.dist * math.cos(diff) + (ufo.rad ** 2 - (ufo.dist * math.sin(diff)) ** 2) ** (1 / 2) > R:
            return True
    return False

def shoot(ufos, laser, R):
    remove_lst = []
    for (i, ufo) in enumerate(ufos):
        if is_dead(ufo, laser, R):
            remove_lst.append(i)
    for i in reversed(remove_lst):
        ufos.pop(i)

def calculate_invading_ufos(R, ufos):
    ufos_objects = [Ufo(x0, y0, r, v) for x0, y0, r, v in ufos]
    ans = 0
    while ufos_objects:
        ans += reache(ufos_objects, R)
        if ufos_objects:
            laser = min(ufos_objects, key=lambda ufo: ufo.dist).angle
            shoot(ufos_objects, laser, R)
    return ans
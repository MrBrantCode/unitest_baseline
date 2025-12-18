"""
QUESTION:
In 20XX AD, a school competition was held. The tournament has finally left only the final competition. You are one of the athletes in the competition.

The competition you participate in is to compete for the time it takes to destroy all the blue objects placed in the space. Athletes are allowed to bring in competition guns. In the space, there are multiple blue objects, the same number of red objects, and multiple obstacles. There is a one-to-one correspondence between the blue object and the red object, and the blue object must be destroyed by shooting a bullet at the blue object from the coordinates where the red object is placed. The obstacles placed in the space are spherical and the composition is slightly different, but if it is a normal bullet, the bullet will stop there when it touches the obstacle.

The bullet used in the competition is a special bullet called Magic Bullet. This bullet can store magical power, and when the bullet touches an obstacle, it automatically consumes the magical power, and the magic that the bullet penetrates is activated. Due to the difference in the composition of obstacles, the amount of magic required to penetrate and the amount of magic power consumed to activate it are different. Therefore, even after the magic for one obstacle is activated, it is necessary to activate another magic in order to penetrate another obstacle. Also, if the bullet touches multiple obstacles at the same time, magic will be activated at the same time. The amount of magical power contained in the bullet decreases with each magic activation.

While the position and size of obstacles and the amount of magical power required to activate the penetrating magic have already been disclosed, the positions of the red and blue objects have not been disclosed. However, the position of the object could be predicted to some extent from the information of the same competition in the past. You want to save as much magical power as you can, because putting magical power into a bullet is very exhausting. Therefore, assuming the position of the red object and the corresponding blue object, the minimum amount of magical power required to be loaded in the bullet at that time, that is, the magical power remaining in the bullet when reaching the blue object is 0. Let's find the amount of magical power that becomes.

Constraints

* 0 ≤ N ≤ 50
* 1 ≤ Q ≤ 50
* -500 ≤ xi, yi, zi ≤ 500
* 1 ≤ ri ≤ 1,000
* 1 ≤ li ≤ 1016
* -500 ≤ sxj, syj, szj ≤ 500
* -500 ≤ dxj, dyj, dzj ≤ 500
* Obstacles are never stuck in other obstacles
* The coordinates of the object are not inside or on the surface of the obstacle
* Under each assumption, the coordinates of the red object and the blue object do not match.

Input

All inputs are integers. Each number is separated by a single space.


N Q
x1 y1 z1 r1 l1
::
xN yN zN rN lN
sx1 sy1 sz1 dx1 dy1 dz1
::
sxQ syQ szQ dxQ dyQ dzQ


* N is the number of obstacles, and Q is the number of coordinates of the assumed blue and red objects.
* xi, yi, and zi are the x-coordinate, y-coordinate, and z-coordinate that represent the position of the center of the i-th obstacle, respectively.
* ri is the radius of the i-th obstacle.
* li is the amount of magical power consumed by magic to penetrate the i-th obstacle.
* sxj, syj, and szj are the x-coordinate, y-coordinate, and z-coordinate that represent the position of the red object in the jth assumption, respectively.
* dxj, dyj, and dzj are the x-coordinate, y-coordinate, and z-coordinate that represent the position of the blue object in the jth assumption, respectively.

Output

Assuming the position of each pair of red objects and the corresponding blue objects, the amount of magical power to be loaded in the bullet is output on one line, assuming that there are only obstacles, red objects, and one pair of blue objects in space. Let's do it. The bullet is supposed to fly in a straight line from the position of the red object to the position of the blue object, and since the size of the bullet is very small, it is treated as a point.

Examples

Input

5 1
0 10 0 5 2
0 20 0 5 12
0 30 0 5 22
0 40 0 5 32
0 50 0 5 42
0 0 0 0 60 0


Output

110


Input

1 1
10 5 0 5 9
0 0 0 9 12 0


Output

9


Input

5 5
-38 -71 -293 75 1
-158 -38 -405 66 1
-236 -303 157 266 1
316 26 411 190 1
207 -312 -27 196 1
-50 292 -375 -401 389 -389
460 278 409 -329 -303 411
215 -220 -200 309 -474 300
261 -494 -87 -300 123 -463
386 378 486 -443 -64 299


Output

0
2
1
3
0
"""

def calculate_minimum_magic_power(N, Q, obstacles, object_pairs):
    results = []
    
    for sx, sy, sz, dx, dy, dz in object_pairs:
        ans = 0
        vx = dx - sx
        vy = dy - sy
        vz = dz - sz
        
        for xi, yi, zi, ri, li in obstacles:
            t = 0
            t += vx * (xi - sx)
            t += vy * (yi - sy)
            t += vz * (zi - sz)
            t /= vx ** 2 + vy ** 2 + vz ** 2
            
            len2 = 0
            len2 += (sx + vx * t - xi) ** 2
            len2 += (sy + vy * t - yi) ** 2
            len2 += (sz + vz * t - zi) ** 2
            
            if 0 < t < 1 and len2 <= ri ** 2 + 1e-09:
                ans += li
        
        results.append(ans)
    
    return results
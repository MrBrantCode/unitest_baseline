"""
QUESTION:
Anchored Balloon

A balloon placed on the ground is connected to one or more anchors on the ground with ropes. Each rope is long enough to connect the balloon and the anchor. No two ropes cross each other. Figure E-1 shows such a situation.

<image>
Figure E-1: A balloon and ropes on the ground

Now the balloon takes off, and your task is to find how high the balloon can go up with keeping the rope connections. The positions of the anchors are fixed. The lengths of the ropes and the positions of the anchors are given. You may assume that these ropes have no weight and thus can be straightened up when pulled to whichever directions. Figure E-2 shows the highest position of the balloon for the situation shown in Figure E-1.

<image>
Figure E-2: The highest position of the balloon

Input

The input consists of multiple datasets, each in the following format.

> n
>  x1 y1 l1
>  ...
>  xn yn ln
>

The first line of a dataset contains an integer n (1 ≤ n ≤ 10) representing the number of the ropes. Each of the following n lines contains three integers, xi, yi, and li, separated by a single space. Pi = (xi, yi) represents the position of the anchor connecting the i-th rope, and li represents the length of the rope. You can assume that −100 ≤ xi ≤ 100, −100 ≤ yi ≤ 100, and 1 ≤ li ≤ 300. The balloon is initially placed at (0, 0) on the ground. You can ignore the size of the balloon and the anchors.

You can assume that Pi and Pj represent different positions if i ≠ j. You can also assume that the distance between Pi and (0, 0) is less than or equal to li−1. This means that the balloon can go up at least 1 unit high.

Figures E-1 and E-2 correspond to the first dataset of Sample Input below.

The end of the input is indicated by a line containing a zero.

Output

For each dataset, output a single line containing the maximum height that the balloon can go up. The error of the value should be no greater than 0.00001. No extra characters should appear in the output.

Sample Input


3
10 10 20
10 -10 20
-10 10 120
1
10 10 16
2
10 10 20
10 -10 20
2
100 0 101
-90 0 91
2
0 0 53
30 40 102
3
10 10 20
10 -10 20
-10 -10 20
3
1 5 13
5 -3 13
-3 -3 13
3
98 97 168
-82 -80 193
-99 -96 211
4
90 -100 160
-80 -80 150
90 80 150
80 80 245
4
85 -90 290
-80 -80 220
-85 90 145
85 90 170
5
0 0 4
3 0 5
-3 0 5
0 3 5
0 -3 5
10
95 -93 260
-86 96 211
91 90 177
-81 -80 124
-91 91 144
97 94 165
-90 -86 194
89 85 167
-93 -80 222
92 -84 218
0


Output for the Sample Input


17.3205081
16.0000000
17.3205081
13.8011200
53.0000000
14.1421356
12.0000000
128.3928757
94.1879092
131.1240816
4.0000000
72.2251798






Example

Input

3
10 10 20
10 -10 20
-10 10 120
1
10 10 16
2
10 10 20
10 -10 20
2
100 0 101
-90 0 91
2
0 0 53
30 40 102
3
10 10 20
10 -10 20
-10 -10 20
3
1 5 13
5 -3 13
-3 -3 13
3
98 97 168
-82 -80 193
-99 -96 211
4
90 -100 160
-80 -80 150
90 80 150
80 80 245
4
85 -90 290
-80 -80 220
-85 90 145
85 90 170
5
0 0 4
3 0 5
-3 0 5
0 3 5
0 -3 5
10
95 -93 260
-86 96 211
91 90 177
-81 -80 124
-91 91 144
97 94 165
-90 -86 194
89 85 167
-93 -80 222
92 -84 218
0


Output

17.3205081
16.0000000
17.3205081
13.8011200
53.0000000
14.1421356
12.0000000
128.3928757
94.1879092
131.1240816
4.0000000
72.2251798
"""

import math

def calculate_max_balloon_height(anchors):
    inf = 10 ** 20
    eps = 1e-07

    def bs(f, mi, ma):
        mm = -1
        while ma > mi + eps:
            m1 = (mi * 2 + ma) / 3.0
            m2 = (mi + ma * 2) / 3.0
            r1 = f(m1)
            r2 = f(m2)
            if r1 < r2:
                mi = m1
            else:
                ma = m2
        return f((ma + mi) / 2.0)

    def f(n):
        a = anchors

        def _f(x, y):
            r = inf
            for (px, py, l) in a:
                r = min(r, l ** 2 - (x - px) ** 2 - (y - py) ** 2)
            return r

        def _fy(y):
            def _ff(x):
                return _f(x, y)
            return bs(_ff, -100, 100)

        r = bs(_fy, -100, 100)
        return r ** 0.5

    return '{:0.7f}'.format(f(len(anchors)))
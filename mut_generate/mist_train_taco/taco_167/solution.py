"""
QUESTION:
During a voyage of the starship Hakodate-maru (see Problem A), researchers found strange synchronized movements of stars. Having heard these observations, Dr. Extreme proposed a theory of "super stars". Do not take this term as a description of actors or singers. It is a revolutionary theory in astronomy.

According to this theory, stars we are observing are not independent objects, but only small portions of larger objects called super stars. A super star is filled with invisible (or transparent) material, and only a number of points inside or on its surface shine. These points are observed as stars by us.

In order to verify this theory, Dr. Extreme wants to build motion equations of super stars and to compare the solutions of these equations with observed movements of stars. As the first step, he assumes that a super star is sphere-shaped, and has the smallest possible radius such that the sphere contains all given stars in or on it. This assumption makes it possible to estimate the volume of a super star, and thus its mass (the density of the invisible material is known).

You are asked to help Dr. Extreme by writing a program which, given the locations of a number of stars, finds the smallest sphere containing all of them in or on it. In this computation, you should ignore the sizes of stars. In other words, a star should be regarded as a point. You may assume the universe is a Euclidean space.



Input

The input consists of multiple data sets. Each data set is given in the following format.


n
x1 y1 z1
x2 y2 z2
...
xn yn zn


The first line of a data set contains an integer n, which is the number of points. It satisfies the condition 4 ≤ n ≤ 30.

The locations of n points are given by three-dimensional orthogonal coordinates: (xi, yi, zi) (i = 1,..., n). Three coordinates of a point appear in a line, separated by a space character.

Each value is given by a decimal fraction, and is between 0.0 and 100.0 (both ends inclusive). Points are at least 0.01 distant from each other.

The end of the input is indicated by a line containing a zero.

Output

For each data set, the radius ofthe smallest sphere containing all given points should be printed, each in a separate line. The printed values should have 5 digits after the decimal point. They may not have an error greater than 0.00001.

Example

Input

4
10.00000 10.00000 10.00000
20.00000 10.00000 10.00000
20.00000 20.00000 10.00000
10.00000 20.00000 10.00000
4
10.00000 10.00000 10.00000
10.00000 50.00000 50.00000
50.00000 10.00000 50.00000
50.00000 50.00000 10.00000
0


Output

7.07107
34.64102
"""

def calculate_smallest_sphere_radius(stars):
    def distance(star, position):
        return sum([(a - b) ** 2 for (a, b) in zip(star, position)]) ** (1 / 2)

    def difference(star, position):
        return [a - b for (a, b) in zip(star, position)]

    n = len(stars)
    position = [sum([s[i] for s in stars]) / n for i in range(3)]
    move_rate = 1

    for i in range(3000):
        if i % 100 == 0:
            move_rate /= 2
        index = 0
        dis_max = 0
        for (j, star) in enumerate(stars):
            dis = distance(star, position)
            if dis_max < dis:
                dis_max = dis
                index = j
        diff = difference(stars[index], position)
        position = [position[i] + diff[i] * move_rate for i in range(3)]

    return round(dis_max, 5)
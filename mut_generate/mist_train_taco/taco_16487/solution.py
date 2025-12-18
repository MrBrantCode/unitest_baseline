"""
QUESTION:
Melody Pond was stolen from her parents as a newborn baby by Madame Kovarian, to become a weapon of the Silence in their crusade against the Doctor. Madame Kovarian changed Melody's name to River Song, giving her a new identity that allowed her to kill the Eleventh Doctor.

Heidi figured out that Madame Kovarian uses a very complicated hashing function in order to change the names of the babies she steals. In order to prevent this from happening to future Doctors, Heidi decided to prepare herself by learning some basic hashing techniques.

The first hashing function she designed is as follows.

Given two positive integers $(x, y)$ she defines $H(x,y):=x^2+2xy+x+1$.

Now, Heidi wonders if the function is reversible. That is, given a positive integer $r$, can you find a pair $(x, y)$ (of positive integers) such that $H(x, y) = r$?

If multiple such pairs exist, output the one with smallest possible $x$. If there is no such pair, output "NO".


-----Input-----

The first and only line contains an integer $r$ ($1 \le r \le 10^{12}$).


-----Output-----

Output integers $x, y$ such that $H(x,y) = r$ and $x$ is smallest possible, or "NO" if no such pair exists.


-----Examples-----
Input
19

Output
1 8

Input
16

Output
NO
"""

import math

def find_smallest_x_y_pair(r):
    for x in range(1, int(math.sqrt(r)) + 1):
        if (pow(x, 2) + x + 1 - r) % (-2 * x) == 0:
            y = (pow(x, 2) + x + 1 - r) // (-2 * x)
            if y > 0:
                return (x, y)
    return "NO"
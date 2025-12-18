"""
QUESTION:
Space Coconut Crab

Space coconut crab

English text is not available in this practice contest.

Ken Marine Blue is a space hunter who travels through the entire galaxy in search of space coconut crabs. The space coconut crab is the largest crustacean in the universe, and it is said that the body length after growth is 400 meters or more, and if you spread your legs, it will reach 1,000 meters or more. Many people have already witnessed the space coconut crab, but none have succeeded in catching it.

Through a long-term study, Ken uncovered important facts about the ecology of space coconut crabs. Surprisingly, the space coconut crab did the same thing as the latest warp technology called phase transition navigation, and lived back and forth between normal space and hyperspace. Furthermore, it was found that it takes a long time for the space coconut crab to warp out from the hyperspace to the normal space, and that it cannot move to the hyperspace for a while after the warp out.

So Ken finally decided to catch the space coconut crab. The strategy is as follows. First, we observe the energy of the space coconut crab as it plunges from normal space into hyperspace. When this energy is e, it is known that the coordinates (x, y, z) at which the space coconut crab warps out of hyperspace satisfy the following conditions.

* x, y, z are all non-negative integers.
* x + y2 + z3 = e.
* Minimize the value of x + y + z under the above conditions.



These conditions alone do not always uniquely determine the coordinates, but it is certain that the coordinates to warp out are on the plane x + y + z = m, where m is the minimum value of x + y + z. Is. Therefore, a barrier of sufficient size is placed on this plane. Then, the space coconut crab will warp out to the place where the barrier is stretched. Space coconut crabs affected by the barrier get stuck. It is a setup to capture it with the weapon breaker, which is a state-of-the-art spacecraft operated by Ken.

The barrier can only be set once, so it cannot fail. So Ken decided to use a calculator to carry out his mission. Your job is to write a program that finds the plane x + y + z = m to which the barrier should be placed when the energy for the space coconut crab to enter the hyperspace is given. Your program will be accepted when it outputs the correct results for all of the prepared test cases.

Input

The input consists of multiple datasets. Each dataset consists of only one row and contains one positive integer e (e ≤ 1,000,000). This represents the energy when the space coconut crab rushes into hyperspace. The input ends when e = 0, which is not included in the dataset.

Output

For each dataset, output the value of m on one line. The output must not contain any other characters.

Sample Input


1
2
Four
27
300
1250
0


Output for the Sample Input


1
2
2
3
18
44






Example

Input

1
2
4
27
300
1250
0


Output

1
2
2
3
18
44
"""

import math

def find_minimum_m(e):
    k = 2 ** 32
    for z in range(100, -1, -1):
        z3 = z * z * z
        if z3 > e:
            continue
        e2 = e - z3
        ylm = int(math.sqrt(e2))
        xzlm = 3 * z * z + 3 * z + 1
        for y in range(ylm, -1, -1):
            y2 = y * y
            if e2 > (y + 1) * (y + 1):
                break
            e3 = e2 - y2
            xylm = 2 * y + 1
            x = e3
            if x > xylm or x > xzlm:
                continue
            k = min(k, x + y + z)
    return k
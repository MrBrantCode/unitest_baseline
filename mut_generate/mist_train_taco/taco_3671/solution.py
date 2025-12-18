"""
QUESTION:
ACM countries have rivers that flow from east to west in the center. This river flows from the neighboring country in the west through the neighboring country in ACM to the neighboring country in the east, and the total length in ACM is K km. It is planned to install several locks on this river and use it as a canal.

A lock is a mechanism for a ship to move between two different water levels. Locks have locks on the upstream and downstream sides, respectively, and a small body of water called a lock chamber between them. After putting the ship in this lock room, water is injected or drained, and the water level in the lock room is raised or lowered to raise or lower the ship. The schematic diagram is shown below.

<image>
Figure F-1: Schematic diagram of the lock

Since the width of this river is not very wide, it has been decided that it will be a one-way canal from west to east. The person in charge of design wants to optimize the location of the lock according to the expected navigation schedule of the ship in order to operate the canal efficiently.

You are a programmer hired by a designer. Your job is to write a program that simulates the time it takes for all ships to cross the river, given the lock information and the navigation schedules for multiple ships.

Each lock is represented by the following information.

* Distance from the western end of ACM country X (km)
* Volume of water required to switch the water level L (L)
* Maximum water injection amount per unit time F (L / h)
* Maximum displacement per unit time D (L / h)
* Hierarchical relationship between the water level on the west side and the water level on the east side of the lock



For convenience, in the simulation, it is assumed that the river continues infinitely outside the ACM as well.

At the start of the simulation, the water levels in all the lock chambers are the lower of the eastern and western water levels. In addition, the ships included in the navigation schedule shall be lined up every 1 km from east to west in the order given by input, starting from the western end of the ACM country. For convenience, the initial position of the leading ship is set to the 0km point.

As soon as the simulation starts, the ship begins to sail east. At this time, no other ship should enter less than 1km before and after one ship. The maximum speed V (km / h) is set for each ship. The ship can reach any speed in an instant and even stand still in an instant. Basically, a ship sails at the maximum speed, but if the following ship has a faster maximum speed than the preceding ship and the following ship catches up 1 km before the preceding ship, the following ship will lead. It sails at the same speed as the ship. The size of the ship and locks shall be negligible.

A ship can enter the lock only when the water level on the west side of the lock is equal to the water level in the lock chamber. Similarly, you can exit the lock only when the water level on the east side of the lock is equal to the water level in the lock chamber. If there is no ship inside, the water level in each lock will rise or fall until it matches the water level on the west side of the lock. If there is a ship, it will be displaced until it matches the water level on the east side of the lock. Even if the ship is moored just 1km away from the lock, the ship can leave the lock. However, at this time, the ship must berth at the exit from the lock until the preceding ship starts.

After passing the eastern end of the ACM country, the ship sails to infinity as fast as possible. The simulation ends when all ships have passed the eastern end of the ACM country.



Input

The input consists of multiple datasets. Each dataset is given in the following format.

> NMK
> X1 L1 F1 D1 UD1
> X2 L2 F2 D2 UD2
> ...
> XN LN FN DN UDN
> V1
> V2
> ...
> VM
>

The first line consists of three integers N, M, K. N (1 ≤ N ≤ 100) is the number of locks, M (1 ≤ M ≤ 100) is the number of ships, and K (2 ≤ K ≤ 1000) is the total length of the river in ACM.

The following N lines represent lock information. Each line consists of 5 integers Xi, Li, Fi, Di, UDi. Xi (1 ≤ Xi ≤ K -1) is the position of lock i from the western end of the ACM country (km), Li (1 ≤ Li ≤ 1000) is the volume of water required to switch the water level of lock i (L), Fi (1 ≤ Fi ≤ 1000) is the maximum water injection amount per unit time of lock i (L / h), Di (1 ≤ Di ≤ 1000) is the maximum drainage amount per unit time of lock i (L / h), UDi ( UDi ∈ {0, 1}) represents the hierarchical relationship between the water level on the west side and the water level on the east side of the lock i, respectively. When UDi is 0, the lock i means that the water level is higher on the east side than on the west side. On the other hand, when UDi is 1, lock i means that the water level is lower on the east side than on the west side.

The following M rows are given the integer Vi (1 ≤ Vi ≤ 1000), which represents the maximum speed (km / h) of the i-th vessel in each row.

Locks are given in ascending order of Xi values. In addition, multiple locks will not be installed at the same position.

The end of the input consists of three zeros separated by spaces.

Output

For each dataset, output the time from the start to the end of the simulation in one line. The output value may contain an error of 10-6 or less. The value may be displayed in any number of digits after the decimal point.

Example

Input

1 1 100
50 200 20 40 0
1
2 4 100
7 4 1 4 1
19 5 1 4 0
5
3
7
9
1 2 3
1 1 1 1 0
1
3
1 2 10
5 10 1 1 1
2
3
0 0 0


Output

110
46.6666666667
5
41.6666666667
"""

def simulate_ship_crossing_time(n, m, k, locks, ship_speeds):
    t_out = [0.0] * (k + m + 1)
    tl_east = [0.0] * (k + m + 1)
    tl_west = [0.0] * (k + m + 1)
    
    for xi, li, fi, di, udi in locks:
        if not udi:
            tl_east[xi] = li / fi
            tl_west[xi] = li / di
            t_out[xi] = -tl_west[xi]
        else:
            tl_east[xi] = li / di
            tl_west[xi] = li / fi
    
    for i, vi in enumerate(ship_speeds):
        t_out[0] = max(t_out[1] - tl_east[1], i / vi)
        for j in range(1, k + m):
            t_out[j] = tl_east[j] + max(t_out[j - 1] + 1 / vi, t_out[j] + tl_west[j], t_out[j + 1] - tl_east[j + 1])
    
    return t_out[k]
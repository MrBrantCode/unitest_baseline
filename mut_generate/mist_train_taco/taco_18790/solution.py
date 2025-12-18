"""
QUESTION:
There is Kannon-do in the mountain behind Ichiro's house. There are 30 steps from the foot to this Kannon-do, and Ichiro goes to Kannon-do almost every day. Ichiro can go up the stairs up to 3 steps with one foot. While playing, I noticed that there are so many types of stair climbing (the number of steps to skip).

So I decided to do 10 different climbs a day and try all the climbs. However, if you are familiar with mathematics, you should know that such a thing will end the life of Ichiro.

In order to convince Ichiro that Ichiro's plan is not feasible, Ichiro will enter all the steps of the stairs n and make 10 different ways of climbing a day. Create a program that outputs the number of years required to execute. Calculate a year as 365 days. If you need even one day, it will be one year. 365 days is one year, and 366 days is two years.



Input

A sequence of multiple datasets is given as input. The end of the input is indicated by a single line of zeros. For each dataset, one integer n (1 ≤ n ≤ 30) representing the number of stages is given on one line.

The number of datasets does not exceed 30.

Output

For each dataset, Ichiro outputs the number of years (integer) required to execute all the climbs on one line.

Example

Input

1
10
20
25
0


Output

1
1
34
701
"""

def calculate_years_to_complete_climbs(n: int) -> int:
    # Precompute the number of ways to climb up to 30 steps
    f = [1, 1, 2, 4]
    while len(f) <= 30:
        f.append(f[-1] + f[-2] + f[-3])
    
    # Calculate the number of days required for n steps
    day = f[n]
    
    # Calculate the number of years
    if day % 3650 == 0:
        return day // 3650
    else:
        return day // 3650 + 1
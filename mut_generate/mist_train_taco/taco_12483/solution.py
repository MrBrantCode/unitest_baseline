"""
QUESTION:
Problem

Neat lives on the world line for a total of 360 days until the 30th of every month for 1 year and 12 months. In that world, N consecutive holidays with the same schedule were applied to people all over the world every year. Consecutive holidays i are consecutive Vi days starting from Mi month Di day.

NEET is NEET, so he is closed every day regardless of consecutive holidays. One day NEET decided to go out unusually, but I hate crowds, so I don't want to go out as much as possible on busy days due to the effects of consecutive holidays. Therefore, Neat is trying to find the day with the least congestion by calculating the congestion degree of each day by the following method.

* The number that represents the degree of influence of a date x by the holiday i is Si if the date x is included in the holiday i, otherwise max (0, Si − min (from x). The number of days until the first day of consecutive holidays i, the number of days from the last day of consecutive holidays i to x)))
* The degree of congestion on a certain date x is the degree of influence that is most affected by N consecutive holidays.



Please output the lowest degree of congestion in the year. However, consecutive holidays i may span years. In addition, the dates of consecutive holidays may overlap.

Constraints

The input satisfies the following conditions.

* 1 ≤ N ≤ 100
* 1 ≤ Mi ≤ 12
* 1 ≤ Di ≤ 30
* 1 ≤ Vi, Si ≤ 360

Input

The input is given in the following format.


N
M1 D1 V1 S1
M2 D2 V2 S2
...
MN DN VN SN


The integer N is given on the first line.
The integers Mi, Di, Vi, Si are given on the 2nd to N + 1th lines separated by blanks. (1 ≤ i ≤ N)

Output

Outputs the least congestion level on one line.

Examples

Input

1
1 1 359 1


Output

0


Input

2
2 4 25 306
1 9 7 321


Output

158


Input

8
2 9 297 297
8 6 359 211
8 16 28 288
7 9 113 143
3 18 315 190
10 18 277 300
9 5 276 88
3 5 322 40


Output

297
"""

def find_lowest_congestion(N, holidays):
    C = [0] * 360
    
    for holiday in holidays:
        Mi, Di, Vi, Si = holiday
        i_start = (Mi - 1) * 30 + Di - 1
        i_end = i_start + Vi - 1
        
        for j in range(i_start, i_end + 1):
            C[j % 360] = max(C[j % 360], Si)
        
        for k in range(1, Si + 1):
            C[(i_start - k + 360) % 360] = max(C[(i_start - k + 360) % 360], Si - k)
            C[(i_end + k) % 360] = max(C[(i_end + k) % 360], Si - k)
    
    return min(C)
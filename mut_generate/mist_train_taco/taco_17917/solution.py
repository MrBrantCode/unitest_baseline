"""
QUESTION:
Vasya has n days of vacations! So he decided to improve his IT skills and do sport. Vasya knows the following information about each of this n days: whether that gym opened and whether a contest was carried out in the Internet on that day. For the i-th day there are four options:

  on this day the gym is closed and the contest is not carried out;  on this day the gym is closed and the contest is carried out;  on this day the gym is open and the contest is not carried out;  on this day the gym is open and the contest is carried out. 

On each of days Vasya can either have a rest or write the contest (if it is carried out on this day), or do sport (if the gym is open on this day).

Find the minimum number of days on which Vasya will have a rest (it means, he will not do sport and write the contest at the same time). The only limitation that Vasya has — he does not want to do the same activity on two consecutive days: it means, he will not do sport on two consecutive days, and write the contest on two consecutive days.


-----Input-----

The first line contains a positive integer n (1 ≤ n ≤ 100) — the number of days of Vasya's vacations.

The second line contains the sequence of integers a_1, a_2, ..., a_{n} (0 ≤ a_{i} ≤ 3) separated by space, where: 

  a_{i} equals 0, if on the i-th day of vacations the gym is closed and the contest is not carried out;  a_{i} equals 1, if on the i-th day of vacations the gym is closed, but the contest is carried out;  a_{i} equals 2, if on the i-th day of vacations the gym is open and the contest is not carried out;  a_{i} equals 3, if on the i-th day of vacations the gym is open and the contest is carried out.


-----Output-----

Print the minimum possible number of days on which Vasya will have a rest. Remember that Vasya refuses:

  to do sport on any two consecutive days,  to write the contest on any two consecutive days. 


-----Examples-----
Input
4

1 3 2 0


Output
2


Input
7

1 3 3 2 1 2 3


Output
0


Input
2

2 2


Output
1




-----Note-----

In the first test Vasya can write the contest on the day number 1 and do sport on the day number 3. Thus, he will have a rest for only 2 days.

In the second test Vasya should write contests on days number 1, 3, 5 and 7, in other days do sport. Thus, he will not have a rest for a single day.

In the third test Vasya can do sport either on a day number 1 or number 2. He can not do sport in two days, because it will be contrary to the his limitation. Thus, he will have a rest for only one day.
"""

def min_rest_days(n, a):
    s = None  # s will track the last activity: 1 for contest, 2 for sport, None for rest
    r = 0  # r will count the number of rest days
    
    for i in range(n):
        if a[i] == 0:
            r += 1  # Rest day
            s = 0  # Reset last activity
        elif a[i] == 1:
            if s == 1:
                r += 1  # Rest day because last activity was also contest
                s = 0  # Reset last activity
                continue
            else:
                s = 1  # Write contest
        elif a[i] == 2:
            if s == 2:
                r += 1  # Rest day because last activity was also sport
                s = 0  # Reset last activity
                continue
            else:
                s = 2  # Do sport
        elif a[i] == 3:
            if s == 1:
                s = 2  # Switch from contest to sport
            elif s == 2:
                s = 1  # Switch from sport to contest
            else:
                # If no previous activity, choose based on next day if possible
                if i != n - 1:
                    if a[i + 1] == 1:
                        s = 2  # Choose sport to avoid contest on next day
                    elif a[i + 1] == 2:
                        s = 1  # Choose contest to avoid sport on next day
                else:
                    s = 1  # Default to contest if no next day
    
    return r
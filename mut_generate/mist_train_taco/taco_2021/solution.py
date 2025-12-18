"""
QUESTION:
Osaki

Osaki

English text is not available in this practice contest.

The Yamanote Line is a circular railway line laid in the 23 wards of Tokyo. The total route distance is 34.5km, and one lap takes about one hour. There are 29 stations in total. The line color is Uguisu color. The peak congestion rate exceeds 200%, making it one of the busiest railway lines in Japan. One train runs every three minutes during the busiest hours, and people who come to Tokyo for the first time are amazed at the sight.

Mr. Tetsuko loves the Yamanote Line and loves genuine railways. One day, she came up with the following question while reading her favorite book, the JR timetable. "How many vehicles are used a day on the Yamanote Line?"

She tried to figure out the minimum number of vehicles required for operation from the timetable. However, the number of trains was so large that she couldn't count it by herself. So she turned to you, a good programmer, for help.

Your job is to write a program to find the minimum number of cars required to operate the Yamanote Line from a given timetable. Since the Yamanote Line is a circular line, the timetable is often written with "Osaki Station" as the starting and ending stations for convenience. Therefore, only the departure and arrival times of each train at Osaki Station are recorded in the timetable given by her.

Although this cannot happen on the actual Yamanote Line, in order to simplify the situation setting, we will consider that the train can depart from Osaki Station immediately after it arrives at Osaki Station. In addition, there are cases where the time taken by Mr. Tetsuko is incorrect, or the train added by Mr. Tetsuko's delusion is mixed in the timetable, but you can not see them, so to the last The number must be calculated for the time as written.

If you write a program that works, she may invite you to a date on the train. However, it is up to you to accept or decline the invitation.

Input

The input consists of multiple datasets. Each dataset has the following format.

> n
> hh: mm: ss hh: mm: ss
> hh: mm: ss hh: mm: ss
> ...
> hh: mm: ss hh: mm: ss

The integer n in the first line is the number of trains included in the timetable. This value is guaranteed not to exceed 10,000. The departure time and arrival time of each train at Osaki Station are given in this order on the n lines from the 2nd line to the n + 1st line, and the departure time and arrival time are separated by a single space. Each time is expressed in the format hh: mm: ss, where hh is the hour, mm is the minute, and ss is the second. The range of each value is 0 ≤ hh <24, 0 ≤ mm <60, 0 ≤ ss <60. All of these numbers are prefixed with 0s as needed to be two digits.

Trains that run across 24:00 at night are not included. Therefore, the departure time is always before the arrival time.

The end of input is indicated by n = 0. It is not included in the dataset.

Output

For each dataset, output the minimum number of vehicles required on one line.

Sample Input


3
05:47:15 09:54:40
12:12:59 12:13:00
16:30:20 21:18:53
6
00:00:00 03:00:00
01:00:00 03:00:00
02:00:00 03:00:00
03:00:00 04:00:00
03:00:00 05:00:00
03:00:00 06:00:00
0


Output for the Sample Input


1
3






Example

Input

3
05:47:15 09:54:40
12:12:59 12:13:00
16:30:20 21:18:53
6
00:00:00 03:00:00
01:00:00 03:00:00
02:00:00 03:00:00
03:00:00 04:00:00
03:00:00 05:00:00
03:00:00 06:00:00
0


Output

1
3
"""

def calculate_minimum_vehicles(timetable):
    if not timetable:
        return 0
    
    # Sort the timetable based on departure times
    timetable.sort(key=lambda x: x[0])
    
    # Initialize variables
    usecar = 0
    returntime = []
    
    for dept, ariv in timetable:
        new = True
        for ariv_time in returntime:
            if ariv_time <= dept:
                new = False
                returntime.remove(ariv_time)
                break
        if new:
            usecar += 1
        returntime.append(ariv)
    
    return usecar
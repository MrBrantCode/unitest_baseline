"""
QUESTION:
Based on the information of the time when study started and the time when study ended, check whether the total time studied in one day is t or more, and if not, create a program to find the shortage time. Time is one unit per hour, and minutes and seconds are not considered. The time is expressed in 24-hour notation in 1-hour units.

Enter the target time of study per day and the information of the time actually studied (number of studies n, start time s and end time f of each study), and check whether the total study time has reached the target. If it has reached, write "OK", and if it has not reached, write a program that outputs the insufficient time. However, the study time spent on each will not overlap.

Example: Target time | Study time | Judgment
--- | --- | ---
10 hours | 6:00 to 11:00 = 5 hours
12:00 to 15:00 = 3 hours
18:00 to 22:00 = 4 hours | OK
14 hours | 6:00 to 11:00 = 5 hours
13:00 to 20:00 = 7 hours
| 2 hours shortage


Input example


Ten
3
6 11
12 15
18 22
14
2
6 11
13 20
0


Output example


OK
2




input

Given a sequence of multiple datasets. The end of the input is indicated by a single line of zeros. Each dataset is given in the following format:


t
n
s1 f1
s2 f2
::
sn fn


The first line gives the target time of the day t (0 ≤ t ≤ 22), and the second line gives the number of studies n (1 ≤ n ≤ 10). The following n lines are given the start time si and end time f (6 ≤ si, fi ≤ 22) of the i-th study.

The number of datasets does not exceed 100.

output

Outputs OK or missing time on one line for each dataset.

Example

Input

10
3
6 11
12 15
18 22
14
2
6 11
13 20
0


Output

OK
2
"""

def check_study_time(target_time: int, study_sessions: list) -> str:
    """
    Check whether the total study time meets the target time.
    
    Parameters:
    - target_time (int): The target study time per day.
    - study_sessions (list of tuples): A list where each tuple contains the start and end times of a study session.
    
    Returns:
    - str: "OK" if the total study time meets or exceeds the target time.
    - int: The shortage time if the total study time is less than the target time.
    """
    total_study_time = sum((f - s for s, f in study_sessions))
    shortage_time = target_time - total_study_time
    
    return "OK" if shortage_time <= 0 else shortage_time
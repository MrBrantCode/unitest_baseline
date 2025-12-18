"""
QUESTION:
Vlad, like everyone else, loves to sleep very much.

Every day Vlad has to do $n$ things, each at a certain time. For each of these things, he has an alarm clock set, the $i$-th of them is triggered on $h_i$ hours $m_i$ minutes every day ($0 \le h_i < 24, 0 \le m_i < 60$). Vlad uses the $24$-hour time format, so after $h=12, m=59$ comes $h=13, m=0$ and after $h=23, m=59$ comes $h=0, m=0$.

This time Vlad went to bed at $H$ hours $M$ minutes ($0 \le H < 24, 0 \le M < 60$) and asks you to answer: how much he will be able to sleep until the next alarm clock.

If any alarm clock rings at the time when he went to bed, then he will sleep for a period of time of length $0$.


-----Input-----

The first line of input data contains an integer $t$ ($1 \le t \le 100$) — the number of test cases in the test.

The first line of the case contains three integers $n$, $H$ and $M$ ($1 \le n \le 10, 0 \le H < 24, 0 \le M < 60$) — the number of alarms and the time Vlad went to bed.

The following $n$ lines contain two numbers each $h_i$ and $m_i$ ($0 \le h_i < 24, 0 \le m_i < 60$) — the time of the $i$ alarm. It is acceptable that two or more alarms will trigger at the same time.

Numbers describing time do not contain leading zeros.


-----Output-----

Output $t$ lines, each containing the answer to the corresponding test case. As an answer, output two numbers  — the number of hours and minutes that Vlad will sleep, respectively. If any alarm clock rings at the time when he went to bed, the answer will be 0 0.


-----Examples-----

Input
3
1 6 13
8 0
3 6 0
12 30
14 45
6 0
2 23 35
20 15
10 30
Output
1 47
0 0
10 55


-----Note-----

None
"""

def calculate_sleep_duration(n, H, M, alarms):
    # Convert the bed time to minutes from the start of the day
    bed_time_in_minutes = H * 60 + M
    
    # Convert each alarm time to minutes from the start of the day
    alarm_times_in_minutes = [h * 60 + m for h, m in alarms]
    
    # Initialize the minimum sleep duration to a large number
    min_sleep_duration = float('inf')
    
    for alarm_time in alarm_times_in_minutes:
        if alarm_time >= bed_time_in_minutes:
            # If the alarm is after the bed time, calculate the difference
            sleep_duration = alarm_time - bed_time_in_minutes
        else:
            # If the alarm is before the bed time, calculate the difference considering the next day
            sleep_duration = (24 * 60 - bed_time_in_minutes) + alarm_time
        
        # Update the minimum sleep duration
        min_sleep_duration = min(min_sleep_duration, sleep_duration)
    
    # Convert the minimum sleep duration back to hours and minutes
    sleep_hours = min_sleep_duration // 60
    sleep_minutes = min_sleep_duration % 60
    
    return (sleep_hours, sleep_minutes)
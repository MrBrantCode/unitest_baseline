"""
QUESTION:
Polycarp has a strict daily schedule. He has n alarms set for each day, and the i-th alarm rings each day at the same time during exactly one minute.

Determine the longest time segment when Polycarp can sleep, i. e. no alarm rings in that period. It is possible that Polycarp begins to sleep in one day, and wakes up in another.


-----Input-----

The first line contains a single integer n (1 ≤ n ≤ 100) — the number of alarms.

Each of the next n lines contains a description of one alarm. Each description has a format "hh:mm", where hh is the hour when the alarm rings, and mm is the minute of that hour when the alarm rings. The number of hours is between 0 and 23, and the number of minutes is between 0 and 59. All alarm times are distinct. The order of the alarms is arbitrary.

Each alarm starts ringing in the beginning of the corresponding minute and rings for exactly one minute (i. e. stops ringing in the beginning of the next minute). Polycarp can start sleeping instantly when no alarm is ringing, and he wakes up at the moment when some alarm starts ringing.


-----Output-----

Print a line in format "hh:mm", denoting the maximum time Polycarp can sleep continuously. hh denotes the number of hours, and mm denotes the number of minutes. The number of minutes should be between 0 and 59. Look through examples to understand the format better.


-----Examples-----
Input
1
05:43

Output
23:59

Input
4
22:00
03:21
16:03
09:59

Output
06:37



-----Note-----

In the first example there is only one alarm which rings during one minute of a day, and then rings again on the next day, 23 hours and 59 minutes later. Polycarp can sleep all this time.
"""

def find_longest_sleep_period(n, alarms):
    def to_minutes(a):
        return 60 * a[0] + a[1]

    def to_hours(a):
        return (a // 60, a % 60)

    def pad(a):
        return ('0' if a < 10 else '') + str(a)

    # Convert all alarm times to minutes and sort them
    alarm_minutes = sorted(to_minutes(alarm) for alarm in alarms)

    longest = 0
    for i in range(1, n):
        longest = max(longest, alarm_minutes[i] - alarm_minutes[i - 1])
    
    # Consider the wrap-around case from the last alarm to the first alarm of the next day
    longest = max(longest, 60 * 24 + alarm_minutes[0] - alarm_minutes[-1])
    
    # Subtract 1 minute because the alarm rings for exactly one minute
    longest -= 1
    
    # Convert the longest sleep period back to hours and minutes
    (hours, minutes) = to_hours(longest)
    
    # Format the result as "hh:mm"
    return f"{pad(hours)}:{pad(minutes)}"
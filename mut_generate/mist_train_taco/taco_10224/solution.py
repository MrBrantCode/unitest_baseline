"""
QUESTION:
Chef is a very experienced and well-known cook. He has participated in many cooking competitions in the past — so many that he does not even remember them all.
One of these competitions lasted for a certain number of days. The first day of the competition was day $S$ of the week (i.e. Monday, Tuesday etc.) and the last day was day $E$ of the week. Chef remembers that the duration of the competition (the number of days between the first and last day, inclusive) was between $L$ days and $R$ days inclusive. Is it possible to uniquely determine the exact duration of the competition? If so, what is this duration?

-----Input-----
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains two space-separated strings $S$ and $E$, followed by a space and two space-separated integers $L$ and $R$.

-----Output-----
For each test case, print a single line containing:
- the string "impossible" if there is no duration consistent with all given information
- the string "many" if there is more than one possible duration
- one integer — the duration of the competition, if its duration is unique

-----Constraints-----
- $1 \le T \le 10,000$
- $1 \le L \le R \le 100$
- $S$ is one of the strings "saturday", "sunday", "monday", "tuesday", "wednesday", "thursday" or "friday"
- $E$ is one of the strings "saturday", "sunday", "monday", "tuesday", "wednesday", "thursday" or "friday"

-----Subtasks-----
Subtask #1 (100 points): original constraints

-----Example Input-----
3
saturday sunday 2 4
monday wednesday 1 20
saturday sunday 3 5

-----Example Output-----
2
many
impossible
"""

def determine_competition_duration(S, E, L, R):
    days_of_week = ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']
    
    # Calculate the offset between the start and end day
    start_index = days_of_week.index(S)
    end_index = days_of_week.index(E)
    offset = (end_index - start_index + 8) % 7
    
    # Find the first valid duration within the range [L, R]
    valid_duration = None
    for duration in range(L, R + 1):
        if duration % 7 == offset:
            valid_duration = duration
            break
    
    if valid_duration is None:
        return "impossible"
    
    # Check if there are multiple valid durations
    if valid_duration + 7 <= R:
        return "many"
    
    return valid_duration
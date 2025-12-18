"""
QUESTION:
You are in geekworld railway station. You are given train schedule as follows
	arrival_time array contains arrival time of each train
	departure_time array contains departure time of each train
	days array contains the particular day when the trains runs. Also each train arrive and departs on the same day
	You are also given number_of_platforms you have.
You have to tell  if it is possible to run all the trains with the given number of platforms such that no train has to wait.
Note: If 2 trains arrive and depart on the same time on the same day on the same platform then depart the train first then second train arrives. Also time in geekland does not follow 24 hr(HHMM) format. So time can be 2368 or 2398, here 2398 > 2368.
 
Example 1:
Input: n = 6 
arr[] = {900, 940, 950, 1100, 1500, 1800}
dep[] = {910, 1200, 1120, 1130, 1900, 2000}
days[] = {1, 2, 2, 1, 3, 4}
platforms = 2
Output: True
Explanation:
Minimum 2 platforms are required to 
safely arrive and depart all trains.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function minimumPlatform2() which takes the arr, dep, days, platforms as inputs and returns a boolean value wheather it is possible to run all trains such that no train waits.
Constraints:
1 ≤ n ≤ 10^5
0 ≤ arr[i] ≤ dep[i] ≤ 2399
1 ≤ number_of_platforms < 100
1 ≤ days[i] < 100
"""

from collections import defaultdict

def can_run_all_trains(arrival_times, departure_times, days, number_of_platforms):
    schedule = defaultdict(list)
    
    # Populate the schedule dictionary with arrival and departure events
    for day, atime, dtime in zip(days, arrival_times, departure_times):
        schedule[day].extend([(atime, +1), (dtime, -1)])
    
    max_occupancy = float('-inf')
    
    # Process each day's schedule
    for day_schedule in schedule.values():
        day_schedule.sort()  # Sort events by time
        current_occupancy = 0
        
        # Calculate the maximum occupancy for the day
        for _, change in day_schedule:
            current_occupancy += change
            max_occupancy = max(max_occupancy, current_occupancy)
    
    # Check if the maximum occupancy exceeds the number of platforms
    return max_occupancy <= number_of_platforms
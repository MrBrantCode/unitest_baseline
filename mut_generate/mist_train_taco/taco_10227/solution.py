"""
QUESTION:
###Instructions

A time period starting from ```'hh:mm'``` lasting until ```'hh:mm'``` is stored in an array:
```
['08:14', '11:34']
```
A set of different time periods is then stored in a 2D Array like so, each in its own sub-array:
```
[['08:14','11:34'], ['08:16','08:18'], ['22:18','01:14'], ['09:30','10:32'], ['04:23','05:11'], ['11:48','13:48'], ['01:12','01:14'], ['01:13','08:15']]
```
Write a function that will take a 2D Array like the above as argument and return a 2D Array of the argument's sub-arrays sorted in ascending order.

Take note of the following:

* The first time period starts at the earliest time  possible ```('00:00'+)```.
* The next time period is the one that starts the soonest **after** the prior time period finishes. If several time periods begin at the same hour, pick the first one showing up in the original array.
* The next time period can start the same time the last one finishes.

This:
```
[['08:14','11:34'], ['08:16','08:18'], ['13:48','01:14'], ['09:30','10:32'], ['04:23','05:11'], ['11:48','13:48'], ['01:12','01:14'], ['01:13','08:15']]
```
Should return:
```
[['01:12','01:14'], ['04:23','05:11'], ['08:14','11:34'], ['11:48','13:48'], ['13:48','01:14'], ['08:16','08:18'], ['09:30','10:32'], ['01:13','08:15']]
```
"""

def sort_time_periods(time_periods):
    # Sort the time periods by their start time
    sorted_periods = sorted(time_periods, key=lambda t: t[0])
    
    # Initialize an empty list to store the sorted sequence of time periods
    sorted_sequence = []
    
    # Loop until all time periods are processed
    while sorted_periods:
        # Find the next time period that starts after the last one in the sorted sequence ends
        next_period_index = next((i for i, t in enumerate(sorted_periods) if not sorted_sequence or t[0] >= sorted_sequence[-1][1]), 0)
        
        # Append the selected time period to the sorted sequence and remove it from the sorted periods list
        sorted_sequence.append(sorted_periods.pop(next_period_index))
    
    return sorted_sequence
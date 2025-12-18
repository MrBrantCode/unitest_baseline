"""
QUESTION:
Write a function called `analyze_profile_data` that takes a string argument `profile_file` representing the path to a profile data file. The function should read the profile data from the file, extract the total time spent in the program (in seconds), time spent in each function (in seconds), and number of calls made to each function, and return these statistics as a dictionary. The dictionary should have the following structure:
```
{
    "total_time": total_time,
    "function_stats": {
        "function1": {
            "time": time_spent,
            "calls": num_calls
        },
        "function2": {
            "time": time_spent,
            "calls": num_calls
        },
        ...
    }
}
```
The function should accurately extract the function names and statistics from the profile data.
"""

import pstats

def analyze_profile_data(profile_file):
    stats = pstats.Stats(profile_file)
    stats.strip_dirs()
    stats.sort_stats('cumulative')
    stats.calc_callees()
    
    total_time = stats.total_tt
    function_stats = {}
    
    for func, (cc, nc, tt, ct, callers) in stats.stats.items():
        function_stats[func] = {
            "time": tt,
            "calls": nc
        }
    
    return {
        "total_time": total_time,
        "function_stats": function_stats
    }
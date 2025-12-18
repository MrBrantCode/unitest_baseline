"""
QUESTION:
You have recently discovered that horses travel in a unique pattern - they're either running (at top speed) or resting (standing still).

Here's an example of how one particular horse might travel:

```
The horse Blaze can run at 14 metres/second for 60 seconds, but must then rest for 45 seconds.

After 500 seconds Blaze will have traveled 4200 metres.
```

Your job is to write a function that returns how long a horse will have traveled after a given time.

####Input: 

* totalTime - How long the horse will be traveling (in seconds)

* runTime - How long the horse can run for before having to rest (in seconds)

* restTime - How long the horse have to rest for after running (in seconds)

* speed - The max speed of the horse (in metres/second)
"""

def calculate_horse_travel_distance(total_time, run_time, rest_time, speed):
    """
    Calculate the total distance a horse will have traveled after a given time,
    given its running and resting patterns.

    Parameters:
    total_time (int): The total time (in seconds) the horse will be traveling.
    run_time (int): The duration (in seconds) the horse can run before needing to rest.
    rest_time (int): The duration (in seconds) the horse needs to rest after running.
    speed (int): The speed (in metres/second) at which the horse runs.

    Returns:
    int: The total distance (in metres) the horse will have traveled after the given total_time.
    """
    cycle_time = run_time + rest_time
    full_cycles, remaining_time = divmod(total_time, cycle_time)
    effective_run_time = full_cycles * run_time + min(remaining_time, run_time)
    distance = effective_run_time * speed
    return distance
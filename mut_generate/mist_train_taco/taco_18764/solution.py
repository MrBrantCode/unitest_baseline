"""
QUESTION:
It's been a tough week at work and you are stuggling to get out of bed in the morning.

While waiting at the bus stop you realise that if you could time your arrival to the nearest minute you could get valuable extra minutes in bed.

There is a bus that goes to your office every 15 minute, the first bus is at `06:00`, and the last bus is at `00:00`.

Given that it takes 5 minutes to walk from your front door to the bus stop, implement a function that when given the curent time will tell you much time is left, before you must leave to catch the next bus.

## Examples

```
"05:00"  =>  55
"10:00"  =>  10
"12:10"  =>  0
"12:11"  =>  14
```

### Notes

1. Return the number of minutes till the next bus
2. Input will be formatted as `HH:MM` (24-hour clock)
3. The input time might be after the buses have stopped running, i.e. after `00:00`
"""

def time_to_next_bus(current_time: str) -> int:
    (h, m) = map(int, current_time.split(':'))
    
    if h < 6:
        # If the time is before 06:00, calculate the time until 06:00
        minutes_until_6 = (5 - h) * 60 + (60 - m)
        if minutes_until_6 > 5:
            return minutes_until_6 - 5
        else:
            return minutes_until_6 + 10
    elif h == 23 and m > 55:
        # If the time is after the last bus at 00:00, calculate the time until the first bus of the next day
        return 355 + (60 - m)
    else:
        # Calculate the time until the next bus within the regular schedule
        minutes_until_next_bus = 15 - (m % 15)
        if minutes_until_next_bus > 4:
            return minutes_until_next_bus - 5
        else:
            return minutes_until_next_bus + 10
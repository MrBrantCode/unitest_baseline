"""
QUESTION:
Write a function `maxValue(events)` that takes a list of events where each event is a list of three integers `[startDay, endDay, value]` and returns the maximum value that can be achieved by attending events without attending multiple events at the same time.

The function should follow these restrictions:

- `1 <= events.length <= 105`
- `events[i].length == 3`
- `1 <= startDayi <= endDayi <= 105`
- `1 <= valuei <= 105`
"""

import bisect
def maxValue(events):
    events.sort(key= lambda x:(x[1], -x[2]))  # sort events based on endDay and value
    dp = [0]*(len(events)+1)
    days = [0] + [e[1] for e in events] # build a new list of sorted endDays.
    for i in range(1, len(events)+1):
        # find the maximum value when we include this current event.
        dp[i] = max(dp[i], dp[bisect.bisect_right(days, events[i-1][0])-1] + events[i-1][2])
        # find the maximum value when we exclude this current event.
        dp[i] = max(dp[i], dp[i-1])
    return dp[-1]
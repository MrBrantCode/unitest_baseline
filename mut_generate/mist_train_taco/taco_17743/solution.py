"""
QUESTION:
In this kata, the number 0 is infected. You are given a list. Every turn, any item in the list that is adjacent to a 0 becomes infected and transforms into a 0. How many turns will it take for the whole list to become infected?

```
[0,1,1,0] ==> [0,0,0,0] 
All infected in 1 turn.

[1,1,0,1,1] --> [1,0,0,0,1] --> [0,0,0,0,0]
All infected in 2 turns

[0,1,1,1] --> [0,0,1,1] --> [0,0,0,1] --> [0,0,0,0]
All infected in 3 turns.
```

All lists will contain at least one item, and at least one zero, and the only items will be 0s and 1s. Lists may be very very long, so pure brute force approach will not work.
"""

def calculate_infection_turns(lst):
    m = 0
    l = 0
    for i, n in enumerate(lst):
        if n == 0:
            m = i if l == 0 else max(m, (i - l + 1) // 2)
            l = i + 1
    return max(m, len(lst) - l)
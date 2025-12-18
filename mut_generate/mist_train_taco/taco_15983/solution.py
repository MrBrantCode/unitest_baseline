"""
QUESTION:
You've had a baby.

Well done. Nice isn't it? Life destroying... but in a good way.

Part of your new routine is lying awake at night worrying that you've either lost the baby... or that you have more than 1!

Given a string of words (x), you need to calculate how many babies are in it. To count as a baby you must have all of the letters in baby ('b', 'a', 'b', 'y'). That counts as 1. They do not need to be in order in the string. Upper and lower case letters count.

Examples:

If there are no babies in the string - you lost the baby!! Return a different value, as shown below:

```if-not:kotlin
'none here' = "Where's the baby?!"
'' = "Where's the baby?!"
```

```if:kotlin 
"none here" = null
"" = null
```
"""

def count_babies(x: str) -> int | str:
    x = x.lower()
    count_a = x.count('a')
    count_b = x.count('b')
    count_y = x.count('y')
    
    # Each "baby" requires 1 'a', 2 'b's, and 1 'y'
    baby_count = min(count_a, count_b // 2, count_y)
    
    return baby_count if baby_count > 0 else "Where's the baby?!"
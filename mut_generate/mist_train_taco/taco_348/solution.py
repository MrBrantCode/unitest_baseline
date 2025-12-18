"""
QUESTION:
How many bees are in the beehive?

* bees can be facing UP, DOWN, LEFT, or RIGHT 
* bees can share parts of other bees

Examples

Ex1
```
bee.bee     
.e..e..
.b..eeb
```
*Answer: 5*


Ex2
```
bee.bee     
e.e.e.e
eeb.eeb
```
*Answer: 8*

# Notes

* The hive may be empty or null/None/nil/...
* Python: the hive is passed as a list of lists (not a list of strings)
"""

from itertools import chain

def count_bees_in_hive(hive):
    if not hive:
        return 0
    
    # Flatten the hive into rows and columns
    rows = map(''.join, hive)
    columns = map(''.join, zip(*hive))
    
    # Count occurrences of 'bee' and 'eeb' in both rows and columns
    bee_count = sum(s.count('bee') + s.count('eeb') for s in chain(rows, columns))
    
    return bee_count
"""
QUESTION:
A group of N golfers wants to play in groups of G players for D days in such a way that no golfer plays more than once with any other golfer. For example, for N=20, G=4, D=5, the solution at Wolfram MathWorld is

```
 Mon:   ABCD    EFGH    IJKL    MNOP    QRST
 Tue:   AEIM    BJOQ    CHNT    DGLS    FKPR
 Wed:   AGKO    BIPT    CFMS    DHJR    ELNQ
 Thu:   AHLP    BKNS    CEOR    DFIQ    GJMT
 Fri:   AFJN    BLMR    CGPQ    DEKT    HIOS
```

Write a function that validates a proposed solution, a list of list of strings, as being a solution to the social golfer problem. Each character represents a golfer, and each string is a group of players. Rows represent days. The solution above would be encoded as:

```
 [
  ['ABCD', 'EFGH', 'IJKL', 'MNOP', 'QRST'],
  ['AEIM', 'BJOQ', 'CHNT', 'DGLS', 'FKPR'],
  ['AGKO', 'BIPT', 'CFMS', 'DHJR', 'ELNQ'],
  ['AHLP', 'BKNS', 'CEOR', 'DFIQ', 'GJMT'],
  ['AFJN', 'BLMR', 'CGPQ', 'DEKT', 'HIOS']
 ]
```

You need to make sure (1) that each golfer plays exactly once every day, (2) that the number and size of the groups is the same every day, and (3) that each player plays with every other player *at most* once.

So although each player must play every day, there can be particular pairs of players that never play together.

It is not necessary to consider the case where the number of golfers is zero; no tests will check for that. If you do wish to consider that case, note that you should accept as valid all possible solutions for zero golfers, who (vacuously) can indeed play in an unlimited number of groups of zero.
"""

def is_valid_social_golfer_solution(solution):
    # Dictionary to track the groups each golfer has played in
    golfer_groups = {}
    
    # Extract the number of days and the number of groups per day
    num_days = len(solution)
    if num_days == 0:
        return True  # Vacuously true for zero golfers
    
    num_groups_per_day = len(solution[0])
    if num_groups_per_day == 0:
        return False  # No groups means no valid solution
    
    group_size = len(solution[0][0])
    if group_size == 0:
        return False  # No golfers in a group means no valid solution
    
    # Set of all golfers
    all_golfers = {golfer for group in solution[0] for golfer in group}
    
    # Validate each day
    for day in solution:
        if len(day) != num_groups_per_day:
            return False  # Number of groups per day must be consistent
        
        for group in day:
            if len(group) != group_size:
                return False  # Group size must be consistent
            
            for golfer in group:
                if golfer not in all_golfers:
                    return False  # All golfers must be known
                
                if golfer not in golfer_groups:
                    golfer_groups[golfer] = set(group) - {golfer}
                else:
                    if len(golfer_groups[golfer] & (set(group) - {golfer})) > 0:
                        return False  # Golfer cannot play with the same person more than once
                    golfer_groups[golfer].update(set(group) - {golfer})
    
    return True
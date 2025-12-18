"""
QUESTION:
# Magpies are my favourite birds

Baby ones even more so...



It is a little known fact^ that the black & white colours of baby magpies differ by **at least** one place and **at most** two places from the colours of the mother magpie.

So now you can work out if any two magpies may be related. 

*...and Quardle oodle ardle wardle doodle the magpies said*

# Kata Task

Given the colours of two magpies, determine if one is a possible **child** or **grand-child** of the other.


# Notes

* Each pair of birds being compared will have same number of colour areas
* `B` = Black
* `W` = White

# Example

Given these three magpies


Magpie 1  BWBWBW
Magpie 2  BWBWBB
Magpie 3  WWWWBB


You can see:
* Magpie 2 may be a child of Magpie 1 because there is only one difference
* Magpie 3 may be child of Magpie 2 because there are two differences
* So Magpie 3 may be a grand-child of Magpie 1
* On the other hand, Magpie 3 cannot be a child of Magpie 1 because there are three differences


---

DM :-)


^ *This fact is little known because I just made it up*
"""

def is_related_magpies(parent_magpie: str, child_magpie: str, relation: str) -> bool:
    def diffs(bird1: str, bird2: str) -> int:
        return sum(c1 != c2 for c1, c2 in zip(bird1, bird2))
    
    if relation == "child":
        return diffs(parent_magpie, child_magpie) in [1, 2]
    elif relation == "grandchild":
        if len(parent_magpie) > 1:
            return diffs(parent_magpie, child_magpie) in [0, 1, 2, 3, 4]
        else:
            return parent_magpie == child_magpie
    else:
        raise ValueError("Invalid relation type. Use 'child' or 'grandchild'.")
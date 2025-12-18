"""
QUESTION:
# Story

Old MacDingle had a farm... 

...and on that farm he had

* horses 
* chickens 
* rabbits 
* some apple trees
* a vegetable patch

Everything is idylic in the MacDingle farmyard **unless somebody leaves the gates open**

Depending which gate was left open then...

* horses might run away
* horses might eat the apples
* horses might eat the vegetables
* chickens might run away
* rabbits might run away
* rabbits might eat the vegetables

# Kata Task

Given the state of the farm gates in the evening, your code must return what the farm looks like the next morning when daylight reveals what the animals got up to.

# Legend

* ```H``` horse
* ```C``` chicken
* ```R``` rabbit
* ```A``` apple tree
* ```V``` vegetables
* ```|``` gate (closed), 
* ```\``` or ```/``` gate (open)
* ```.``` everything else

# Example


Before
```|..HH....\AAAA\CC..|AAA/VVV/RRRR|CCC```

After
```|..HH....\....\CC..|AAA/.../RRRR|...```
Because:

The horses ate whatever apples they could get to
The rabbits ate the vegetables
The chickens ran away




# Notes

* If the animals can eat things *and* also run away then they do **BOTH** - it is best not to run away when you are hungry!
* An animal cannot "go around" a closed gate...
* ...but it is possible to run away from the farm and then **RUN BACK** and re-enter though more open gates on the other side!
"""

from itertools import groupby

def simulate_farm_morning(farm):
    who_eats_whom = {'H': ['A', 'V'], 'R': ['V'], 'C': []}
    (runaway_back, runaway_front, farm) = ([], [], [''.join(j) for (k, j) in groupby(farm)])

    def doSomeFarm(i=0):
        def do(j, s=False):
            while (j >= 0 if s else j < len(farm)) and farm[j] != '|':
                if farm[j][0] in who_eats_whom[current[0]]:
                    farm[j] = '.' * len(farm[j])
                j += [1, -1][s]
            return j
        while i < len(farm):
            current = farm[i]
            if current[0] in who_eats_whom:
                (r, r1) = (do(i, 1), do(i))
                if r == -1 or r1 == len(farm):
                    farm[i] = '.' * len(farm[i])
                    [runaway_front, runaway_back][r != -1].append(current[0])
            i += 1
    doSomeFarm()
    l = len(runaway_back)
    if l:
        if farm[0] != '|':
            farm = ['/'] + ' / '.join(runaway_back[::-1]).split() + farm
            doSomeFarm()
            farm = farm[l * 2:]
    l = len(runaway_front)
    if l:
        if farm[-1] != '|':
            farm = farm + ['/'] + ' / '.join(runaway_front).split()
            doSomeFarm()
            farm = farm[:-l * 2]
    return ''.join(farm)
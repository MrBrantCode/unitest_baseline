"""
QUESTION:
Given an array of `n` boxes where each box is represented as `[status, candies, keys, containedBoxes]`, write a function `maxCandies(status, candies, keys, containedBoxes, initialBoxes)` that returns the maximum number of candies you can get by opening boxes and using their keys to open other boxes.

* `status`: an array of integers where `status[i]` is 1 if `box[i]` is open and 0 if `box[i]` is closed.
* `candies`: an array of integers representing the number of candies in each box.
* `keys`: an array of arrays where `keys[i]` contains the indices of the boxes you can open with the key in `box[i]`.
* `containedBoxes`: an array of arrays where `containedBoxes[i]` contains the indices of the boxes found in `box[i]`.
* `initialBoxes`: an array of indices of the boxes you start with.

Constraints:
* `1 <= status.length <= 1000`
* `status.length == candies.length == keys.length == containedBoxes.length == n`
* `status[i]` is 0 or 1.
* `1 <= candies[i] <= 1000`
* All values in `keys[i]` and `containedBoxes[i]` are unique.
* Each box is contained in one box at most.
* `0 <= initialBoxes.length <= status.length`
* `0 <= initialBoxes[i] < status.length`
"""

import collections

def entrance(status, candies, keys, containedBoxes, initialBoxes):
    n = len(status)
    queue = collections.deque(initialBoxes)
    unopened = set()
    collected = 0
    for box in queue:
        if status[box] == 1:
            collected += candies[box]
            for key in keys[box]:
                if key in unopened:
                    unopened.remove(key)
                    queue.append(key)
                else:
                    status[key] = 1
            for box2 in containedBoxes[box]:
                if status[box2] == 1:
                    queue.append(box2)
                else:
                    unopened.add(box2)
        else:
            unopened.add(box)
    while unopened:
        found = False
        for box in list(unopened):
            if status[box] == 1:
                found = True
                collected += candies[box]
                unopened.remove(box)
                for key in keys[box]:
                    if key in unopened:
                        unopened.remove(key)
                        queue.append(key)
                    else:
                        status[key] = 1
                for box2 in containedBoxes[box]:
                    if status[box2] == 1:
                        queue.append(box2)
                    else:
                        unopened.add(box2)
        if not found:
            break
    return collected
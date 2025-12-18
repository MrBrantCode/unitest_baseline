"""
QUESTION:
Design a data structure that supports all following operations in average O(1) time.



insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.



Example:

// Init an empty set.
RandomizedSet randomSet = new RandomizedSet();

// Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomSet.insert(1);

// Returns false as 2 does not exist in the set.
randomSet.remove(2);

// Inserts 2 to the set, returns true. Set now contains [1,2].
randomSet.insert(2);

// getRandom should return either 1 or 2 randomly.
randomSet.getRandom();

// Removes 1 from the set, returns true. Set now contains [2].
randomSet.remove(1);

// 2 was already in the set, so return false.
randomSet.insert(2);

// Since 2 is the only number in the set, getRandom always return 2.
randomSet.getRandom();
"""

import random

def randomized_set_operations(operation, val=None, state=None):
    if state is None:
        state = {'dic': {}, 'l': []}
    
    if operation == "insert":
        if val in state['dic']:
            return False, state
        state['l'].append(val)
        state['dic'][val] = len(state['l']) - 1
        return True, state
    
    elif operation == "remove":
        if val not in state['dic']:
            return False, state
        index = state['dic'][val]
        last_element = state['l'][-1]
        state['dic'][last_element] = index
        state['l'][index], state['l'][-1] = state['l'][-1], state['l'][index]
        state['l'].pop()
        del state['dic'][val]
        return True, state
    
    elif operation == "getRandom":
        if not state['l']:
            raise ValueError("Set is empty")
        random_element = random.choice(state['l'])
        return random_element, state
    
    else:
        raise ValueError("Invalid operation")
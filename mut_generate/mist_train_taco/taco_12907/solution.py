"""
QUESTION:
Design and implement a data structure for a Least Frequently Used (LFU) cache.
Implement the given LFUCache Class with the following description.
LFUCache(int capacity): This Initializes the object with the capacity of the data structure.
int get(int key): Returns the value of the given key if it exists or else returns -1.
void put(int key, int value): If the key is already present, then update its value and if the key is not present, then it should be inserted. If the data  structure has reached its maximum capacity, then the least frequently used (LFU) key should be invalidated and removed. If during removal, more than one key has same frequency, then the Least Recently Used (LRU) key amongst them should be removed.
Example:
Input: 
Capacity: 3
put(5,7)put(4,6)put(3,5)put(2,4)put(1,3)
get(1)get(2)get(3)get(4)get(5)
Output: 
3
4
5
-1
-1
Explanation: 
When put(2,4) is executed, (5,7) gets invalidated. Similarly when put(1,3) is executed, (4,6) gets invalidated. Therefore only the values for key 1,2,3 are present in the cache after all the put operations.
Your Task:
Implement the given functions, void put(int key, int value) and int get(int key). 
The functions get and put must each run in O(1) average time complexity.
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).
Constraints:
0 <= capacity <= 10^{4}
0 <= key <= 10^{5}
0 <= value <= 10^{6}
At most 2 *10^{5} calls will be made to get and put.
"""

import collections

def lfu_cache_operations(capacity: int, operations: list) -> list:
    def lfu_cache_instance():
        class LFUCache:
            def __init__(self, capacity: int):
                self.capacity = capacity
                self.minfreq = None
                self.keyfreq = {}
                self.freqkeys = collections.defaultdict(collections.OrderedDict)

            def get(self, key: int) -> int:
                if key not in self.keyfreq:
                    return -1
                freq = self.keyfreq[key]
                val = self.freqkeys[freq][key]
                del self.freqkeys[freq][key]
                if not self.freqkeys[freq]:
                    if freq == self.minfreq:
                        self.minfreq += 1
                    del self.freqkeys[freq]
                self.keyfreq[key] = freq + 1
                self.freqkeys[freq + 1][key] = val
                return val

            def put(self, key: int, value: int) -> None:
                if self.capacity <= 0:
                    return
                if key in self.keyfreq:
                    freq = self.keyfreq[key]
                    self.freqkeys[freq][key] = value
                    self.get(key)
                    return
                if self.capacity == len(self.keyfreq):
                    (delkey, delval) = self.freqkeys[self.minfreq].popitem(last=False)
                    del self.keyfreq[delkey]
                self.keyfreq[key] = 1
                self.freqkeys[1][key] = value
                self.minfreq = 1
        
        return LFUCache(capacity)
    
    cache = lfu_cache_instance()
    results = []
    
    for operation in operations:
        op_type = operation[0]
        key = operation[1]
        if op_type == "put":
            value = operation[2]
            cache.put(key, value)
        elif op_type == "get":
            results.append(cache.get(key))
    
    return results
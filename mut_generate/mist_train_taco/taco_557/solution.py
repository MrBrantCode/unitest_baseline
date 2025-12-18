"""
QUESTION:
Design a data structure that works like a LRU Cache. Here cap denotes the capacity of the cache and Q denotes the number of queries. Query can be of two types:
	SET x y: sets the value of the key x with value y 
	GET x: gets the key of x if present else returns -1.
The LRUCache class has two methods get() and set() which are defined as follows.
	get(key): returns the value of the key if it already exists in the cache otherwise returns -1.
	set(key, value): if the key is already present, update its value. If not present, add the key-value pair to the cache. If the cache reaches its capacity it should invalidate the least recently used item before inserting the new item.
	In the constructor of the class the capacity of the cache should be initialized.
 
Example 1:
Input:
cap = 2
Q = 2
Queries = SET 1 2 GET 1
Output: 2
Explanation: 
Cache Size = 2
SET 1 2 GET 1
SET 1 2 : 1 -> 2
GET 1 : Print the value corresponding
to Key 1, ie 2.
Example 2:
Input:
cap = 2
Q = 8
Queries = SET 1 2 SET 2 3 SET 1 5
SET 4 5 SET 6 7 GET 4 SET 1 2 GET 3
Output: 5 -1
Explanation: 
Cache Size = 2
SET 1 2 : 1 -> 2
SET 2 3 : 1 -> 2, 2 -> 3 (the most recently 
used one is kept at the rightmost position) 
SET 1 5 : 2 -> 3, 1 -> 5
SET 4 5 : 1 -> 5, 4 -> 5 (Cache size is 2, hence 
we delete the least recently used key-value pair)
SET 6 7 : 4 -> 5, 6 -> 7 
GET 4 : Prints 5 (The cache now looks like
6 -> 7, 4->5)
SET 1 2 : 4 -> 5, 1 -> 2 
(Cache size is 2, hence we delete the least 
recently used key-value pair)
GET 3 : No key value pair having 
key = 3. Hence, -1 is printed.
Your Task:
You don't need to read input or print anything. Complete the constructor and get(), and set() methods of the class LRUcache. 
Expected Time Complexity: O(1) for both get() and set().
Expected Auxiliary Space: O(1) for both get() and set(). 
(Although, you may use extra space for cache storage and implementation purposes).
Constraints:
1 <= cap <= 10^3
1 <= Q <= 10^5
1 <= x, y <= 10^4
"""

def lru_cache_operations(capacity, queries):
    class Node:
        def __init__(self, key=None, value=None):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None

    class LRUCache:
        def __init__(self, capacity):
            self.capacity = capacity
            self.cache = {}
            self.head = Node()
            self.tail = Node()
            self.head.next = self.tail
            self.tail.prev = self.head

        def get(self, key):
            if key in self.cache:
                node = self.cache[key]
                self._remove(node)
                self._add(node)
                return node.value
            return -1

        def set(self, key, value):
            if key in self.cache:
                node = self.cache[key]
                self._remove(node)
            elif len(self.cache) == self.capacity:
                node = self.tail.prev
                self._remove(node)
                del self.cache[node.key]
            node = Node(key, value)
            self.cache[key] = node
            self._add(node)

        def _add(self, node):
            next_node = self.head.next
            self.head.next = node
            node.prev = self.head
            node.next = next_node
            next_node.prev = node

        def _remove(self, node):
            prev_node = node.prev
            next_node = node.next
            prev_node.next = next_node
            next_node.prev = prev_node

    cache = LRUCache(capacity)
    results = []

    for query in queries:
        if query[0] == 'SET':
            cache.set(query[1], query[2])
        elif query[0] == 'GET':
            results.append(cache.get(query[1]))

    return results
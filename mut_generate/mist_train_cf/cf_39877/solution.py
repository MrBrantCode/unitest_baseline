"""
QUESTION:
Implement the `generate_shingles` function, which takes a string `document` and an integer `k` as input and returns a set of shingles present in the document. A shingle is a sequence of `k` consecutive words in the document. Use minhashing to efficiently generate the shingles by hashing each shingle using MD5 and storing the hashed shingles in a minheap. The function should return the set of unique shingles.

The function signature is:
```python
def generate_shingles(document: str, k: int) -> set:
```
"""

import heapq
import hashlib

def generate_shingles(document: str, k: int) -> set:
    shingles = set()
    min_heap = []
    words = document.split()
    for i in range(len(words) - k + 1):
        shingle = ' '.join(words[i:i + k])
        shingle_hash = hashlib.md5(shingle.encode()).hexdigest()
        heapq.heappush(min_heap, shingle_hash)
    while min_heap:
        shingles.add(heapq.heappop(min_heap))
    return shingles
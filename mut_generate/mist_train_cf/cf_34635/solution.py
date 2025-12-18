"""
QUESTION:
Implement a data structure `_c_id` to efficiently store and retrieve contributions based on incremented spin pair IDs. The data structure should be able to store contributions associated with each incremented spin pair ID and allow retrieval of contributions for a given spin pair ID.

The data structure will be populated with the following information:
- A list of peak objects
- Each peak object has contributions that can be retrieved by `getContributions()`
- Each contribution object has spin pairs that can be retrieved by `getSpinPairs()`
- Each spin pair object has an ID that can be retrieved by `getId()`, which should be incremented by 1 when storing contributions

Implement a method `getContributionsForSpinPairId(spin_pair_id)` that returns the contributions associated with a given spin pair ID.
"""

def getContributionsForSpinPairId(peaks, spin_pair_id):
    _c_id = {}
    for p in peaks:
        for c in p.getContributions():
            for sp in c.getSpinPairs():
                sid = sp.getId() + 1
                if sid not in _c_id:
                    _c_id[sid] = set()
                _c_id[sid].add(c)
    return _c_id.get(spin_pair_id, set())
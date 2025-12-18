"""
QUESTION:
Implement the `get_value(snapshot_index, value_node)` method in the `SnapshotDataStructure` class. The `get_value()` method should take a snapshot index and a value node as input and return the value of the specified node at the given snapshot index. The method should use the `snapshots` dictionary to retrieve the snapshot and then retrieve the value of the specified node. If the snapshot index or value node does not exist, the method should return `None`.
"""

def get_value(snapshot_index, snapshots, value_node):
    if snapshot_index in snapshots:
        snapshot = snapshots[snapshot_index]['snapshot']
        if value_node in snapshot:
            return snapshot[value_node]
    return None
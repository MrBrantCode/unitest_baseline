"""
QUESTION:
Create a function `generate_rsync_commands` that takes two lists of file snapshots (`old_snapshots` and `new_snapshots`) and returns a list of commands to synchronize the files. The function should generate commands for file deletion, copying, and hard-linking based on the differences between the old and new snapshots. The `old_snapshots` list represents the file snapshots from the source system, and the `new_snapshots` list represents the file snapshots from the destination system. Each snapshot is a string representing the file path. The function should not consider file content comparison, delta transfer, and other advanced features.
"""

from typing import List

def generate_rsync_commands(old_snapshots: List[str], new_snapshots: List[str]) -> List[str]:
    commands = []

    for snapshot in old_snapshots:
        if snapshot not in new_snapshots:
            commands.append(f"delete /destination/path/{snapshot.split('/')[-1]}")

    for snapshot in new_snapshots:
        if snapshot not in old_snapshots:
            commands.append(f"copy {snapshot} /destination/path")

    for snapshot in new_snapshots:
        if snapshot in old_snapshots:
            commands.append(f"hardlink {snapshot} /destination/path/{snapshot.split('/')[-1]}")

    return commands
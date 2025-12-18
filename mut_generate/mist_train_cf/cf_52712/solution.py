"""
QUESTION:
Write a function `minOperations(logs)` that takes a list of strings `logs` as input where each string represents a file system operation and returns the minimum number of operations required to return to the main folder after executing all operations in the list.

Each operation in `logs` is one of the following:
- `../` : Move to the parent folder of the current folder (no change if already in the main folder).
- `./` : Stay in the same folder.
- `x/` : Move to the child folder named `x` (folder is guaranteed to exist).

The file system starts in the main folder and executes the operations in `logs` sequentially. The function should return the minimum number of operations needed to return to the main folder after all operations are executed. 

Constraints:
- `1 <= logs.length <= 10^3`
- `2 <= logs[i].length <= 10`
- `logs[i]` contains lowercase English letters, digits, `'.'`, and `'/'`.
- `logs[i]` adheres to the specified format.
- Folder names are composed of lowercase English letters and digits.
"""

def minOperations(logs):
    depth = 0
    for log in logs:
        if log == '../':
            depth = max(0, depth - 1)
        elif log != './':
            depth += 1
    return depth
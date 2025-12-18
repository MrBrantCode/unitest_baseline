"""
QUESTION:
Implement the `traverse_file_system` function to return a list of absolute paths of all files reachable from a given entry point in a file system. The function takes three parameters: `directory` (the root directory), `file_map` (a dictionary representing the file system structure), and `entrypoint` (the absolute path of the entry point). The function should consider all possible edge cases and handle them appropriately.
"""

def traverse_file_system(directory, file_map, entrypoint):
    stack = [entrypoint]
    result = []

    while stack:
        current = stack.pop()
        if current in file_map:
            for item in file_map[current]:
                if item.endswith(".txt"):
                    result.append(current + "/" + item)
                else:
                    stack.append(current + "/" + item)

    return result
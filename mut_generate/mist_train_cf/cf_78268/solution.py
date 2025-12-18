"""
QUESTION:
Implement a function `search_engine` that takes in a query string and a nested list of strings as input, and returns a list of all paths (as lists of indices) leading to the query string. The function should perform a depth-first search and return the paths in the order they are found. The input list can contain nested lists of strings but no other data types. If the query is not found, return an empty list.
"""

def search_engine(query, data):
    def find_paths(query, data, path):
        paths = []
        for i, val in enumerate(data):
            new_path = path + [i]
            if val == query:
                paths.append(new_path)
            elif isinstance(val, list):
                paths.extend(find_paths(query, val, new_path))
        return paths

    return find_paths(query, data, [])
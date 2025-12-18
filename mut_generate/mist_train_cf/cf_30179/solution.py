"""
QUESTION:
Write a function `longestCommonDirectoryPath(filePaths)` that takes in a list of file paths where each file path consists of a sequence of directories separated by slashes ("/"). The function should return the longest common directory path among the file paths. If there is no common directory path, the function should return an empty string. The function must handle an empty list of file paths.
"""

def longestCommonDirectoryPath(filePaths):
    if not filePaths:
        return ""

    paths = [path.split('/') for path in filePaths]
    min_len = min(len(path) for path in paths)
    common_path = []

    for i in range(min_len):
        if all(path[i] == paths[0][i] for path in paths):
            common_path.append(paths[0][i])
        else:
            break

    return '/'.join(common_path)
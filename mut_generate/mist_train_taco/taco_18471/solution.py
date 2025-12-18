"""
QUESTION:
Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"

Corner Cases:


       Did you consider the case where path = "/../"?
       In this case, you should return "/".
       Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
       In this case, you should ignore redundant slashes and return "/home/foo".
"""

def simplify_path(path: str) -> str:
    stack = []
    path = [p for p in path.split('/') if p]
    for f in path:
        if f == '.':
            continue
        elif f == '..':
            if stack:
                stack.pop()
        else:
            stack.append(f)
    return '/' + '/'.join(stack)
"""
QUESTION:
Create a function named `getFolderNames` that takes an array of strings `names` as input and returns an array of strings where each string represents the actual name assigned to a directory. The function should ensure that directory names are unique by appending a suffix in the format of `(k)` if a name already exists, where `k` is the smallest positive integer that ensures the name remains unique. The input array `names` has a length between 1 and 5 * 10^4, and each string in `names` has a length between 1 and 20 and consists of lower case English letters, digits, and/or round brackets.
"""

def getFolderNames(names):
    dir_names = {}
    result = []
    
    for name in names:
        if name not in dir_names:
            dir_names[name] = 0
            result.append(name)
        else:
            while True:
                dir_names[name] += 1
                new_name = name + "(" + str(dir_names[name]) + ")"
                if new_name not in dir_names:
                    dir_names[new_name] = 0
                    result.append(new_name)
                    break
    return result
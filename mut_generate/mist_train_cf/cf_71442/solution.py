"""
QUESTION:
Implement a function `canConvert(str1, str2, k)` that determines whether string `str1` can be transformed into string `str2` by doing zero or more conversions, where in one conversion you can convert all occurrences of one character in `str1` to any other lowercase English character, with a maximum of `k` conversions allowed. Both strings are of the same length and contain only lowercase English letters. Return `true` if and only if `str1` can be transformed into `str2` within the given limit of conversions.
"""

def canConvert(str1, str2, k):
    if str1 == str2:
        return True
    
    dict1 = {}
    dict2 = {}
    for i in range(26):
        dict1[chr(97+i)] = chr(97+i)
        dict2[chr(97+i)] = chr(97+i)

    count = 0
    for i in range(len(str1)):
        if not str1[i] in dict1:
            dict1[str1[i]] = str2[i]

        elif dict1[str1[i]] != str2[i]:
            return False
       
        if not str2[i] in dict2:
            dict2[str2[i]] = str1[i]
            count += 1

        elif dict2[str2[i]] != str1[i]:
            return False

    return count <= k
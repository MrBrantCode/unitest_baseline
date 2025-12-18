"""
QUESTION:
Write a function `compare_freq(str1, str2)` that compares the frequency of each character in two strings and returns a dictionary where the keys are the characters and the values are either the ratio of their appearances in `str1` to `str2` (if they appear in both), or a string indicating which string they only appear in. The comparison should be case insensitive.
"""

def compare_freq(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    dict1 = {}
    dict2 = {}
    
    for i in str1:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1
    
    for j in str2:
        if j in dict2:
            dict2[j] += 1
        else:
            dict2[j] = 1
    
    ratio = {}
    for k in dict1.keys():
        if k in dict2:
            ratio[k] = dict1[k] / dict2[k]
        else:
            ratio[k] = f'Only in first string'
    
    for l in dict2.keys():
        if l not in dict1:
            ratio[l] = f'Only in second string'
    return ratio
"""
QUESTION:
Write a function named `find_longest_substring` that takes two lists of strings as input, finds the longest common starting substring between the first string of each list, and returns this substring. The function should consider only the first string from each list and find the common substring from the start of both strings.
"""

def find_longest_substring(list1, list2):
    string1 = list1[0]
    string2 = list2[0]
    min_length = min(len(string1), len(string2))
    longest_substring = ""
    
    for i in range(min_length):
        if string1[i] == string2[i]:
            longest_substring += string1[i]
        else:
            break
    return longest_substring
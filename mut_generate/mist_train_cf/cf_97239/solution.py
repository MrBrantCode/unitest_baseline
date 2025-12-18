"""
QUESTION:
Write a function `closest_string` that takes two parameters: a string `string` and a list of strings `strings`. The function should return the lexicographically smallest string from `strings` that requires the minimum number of character modifications (insertions, deletions, or substitutions) to transform it into `string`. The length of `string` will be at most 1000 characters, and the length of each string in `strings` will be at most 100 characters. The number of strings in `strings` will be at most 10^5.
"""

def closest_string(string, strings):
    min_distance = float('inf')
    closest_strings = []
    
    for s in strings:
        distance = 0
        if len(string) != len(s):
            distance += abs(len(string) - len(s))
        
        for i in range(min(len(string), len(s))):
            if string[i] != s[i]:
                distance += 1
        
        if len(string) > len(s):
            distance += len(string) - len(s)
        elif len(string) < len(s):
            distance += len(s) - len(string)
        
        if distance < min_distance:
            min_distance = distance
            closest_strings = [s]
        elif distance == min_distance:
            closest_strings.append(s)
    
    closest_strings.sort()
    return closest_strings[0]
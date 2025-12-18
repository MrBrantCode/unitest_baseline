"""
QUESTION:
Write a function `find_shortest_unique_substring` that takes two strings `string1` and `string2` as input and returns the shortest unique substring of `string1` that contains all characters of `string2`, assuming the order of characters in `string2` does not matter. If no such substring exists, return an empty string.
"""

def find_shortest_unique_substring(string1, string2):
    string2_set = set(string2)
    min_length = float('inf')
    min_string = ""

    for i in range(len(string1)):
        visited = set()
        for j in range(i, len(string1)):
            if string1[j] in string2_set:
                visited.add(string1[j])
                if len(visited) == len(string2_set):
                    if j - i + 1 < min_length:
                        min_length = j - i + 1
                        min_string = string1[i:j+1]
                    break

    if min_length == float('inf'):
        return ""
    else:
        return min_string
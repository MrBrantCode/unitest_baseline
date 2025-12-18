"""
QUESTION:
Create a function called `closest_string_match` that takes two parameters: `string` and `strings`, where `string` is a target string and `strings` is a list of strings. The function should return the string in the `strings` list that has the minimum Levenshtein distance to the target `string`. The Levenshtein distance is the minimum number of single-character edits (insertions, deletions or substitutions) required to change one word into the other.
"""

def closest_string_match(string, strings):
    def levenshtein_distance(s1, s2):
        if len(s1) > len(s2):
            s1, s2 = s2, s1

        distances = range(len(s1) + 1)
        for i2, c2 in enumerate(s2):
            distances_ = [i2+1]
            for i1, c1 in enumerate(s1):
                if c1 == c2:
                    distances_.append(distances[i1])
                else:
                    distances_.append(
                        1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
            distances = distances_
        return distances[-1]

    min_distance = float("inf")
    min_string = ""
    for s in strings:
        distance = levenshtein_distance(string, s)
        if distance < min_distance:
            min_distance = distance 
            min_string = s
    return min_string
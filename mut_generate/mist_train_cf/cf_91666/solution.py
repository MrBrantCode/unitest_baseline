"""
QUESTION:
Implement a function `find_closest_match(original_string, target_word)` that finds the closest match in the `original_string` to the `target_word` using the Levenshtein edit distance. If there are multiple closest matches, return the one that appears first in the `original_string`. If there are no matches with an edit distance of 1, return an empty string.
"""

def find_closest_match(original_string, target_word):
    def levenshtein_distance(s1, s2):
        if len(s1) < len(s2):
            return levenshtein_distance(s2, s1)

        if len(s2) == 0:
            return len(s1)

        previous_row = range(len(s2) + 1)

        for i, c1 in enumerate(s1):
            current_row = [i + 1]

            for j, c2 in enumerate(s2):
                insertions = previous_row[j + 1] + 1
                deletions = current_row[j] + 1
                substitutions = previous_row[j] + (c1 != c2)
                current_row.append(min(insertions, deletions, substitutions))

            previous_row = current_row

        return previous_row[-1]

    closest_match = ''
    closest_distance = float('inf')
    
    for word in original_string.split():
        distance = levenshtein_distance(word, target_word)
        
        if distance == 1 and distance < closest_distance:
            closest_match = word
            closest_distance = distance
    
    return closest_match
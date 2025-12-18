"""
QUESTION:
Write a function `shortest_unique_substrings(n, m, p)` that finds the shortest unique sub-string from three input strings `n`, `m`, and `p`. The function should consider non-ASCII characters, be case sensitive, and handle repeating characters and special characters. If no unique sub-string exists, the function should return `None`.
"""

def shortest_unique_substrings(n, m, p):
    # Initialize the length of the shortest unique substring to infinity
    min_len = float('inf')
    result = ""
    
    # Create three sets to store every substring of n, m, and p
    sets = [set(), set(), set()]
    
    # For each string
    for i, string in enumerate([n, m, p]):
        # For each possible substring length
        for sub_len in range(1, len(string) + 1):
            # For each possible start index of the substring
            for start_index in range(0, len(string) - sub_len + 1):
                substring = string[start_index:start_index + sub_len]
                # If the substring is unique across all strings
                if substring not in sets[(i + 1) % 3] and substring not in sets[(i + 2) % 3]:
                    sets[i].add(substring)
                    # If the substring is shorter than the current shortest unique substring
                    if sub_len < min_len:
                        min_len = sub_len
                        result = substring
    
    return result if result else None
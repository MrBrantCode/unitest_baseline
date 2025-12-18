"""
QUESTION:
Implement a function named `generate_permutations` that takes a string `s` as input and returns a list of distinct permutations without using any built-in functions or libraries. The function should handle strings containing duplicate characters and avoid generating duplicate permutations. The time complexity of the function should be O(n!), where n is the length of the string.
"""

def generate_permutations(s):
    perms = []
    
    def permute(prefix, remaining, perms):
        if len(remaining) == 0:
            perms.append(prefix)
        else:
            prev_char = None
            for i in range(len(remaining)):
                if remaining[i] == prev_char:
                    continue
                curr_char = remaining[i]
                permute(prefix + curr_char, remaining[:i] + remaining[i+1:], perms)
                prev_char = curr_char
    
    permute("", s, perms)
    return perms
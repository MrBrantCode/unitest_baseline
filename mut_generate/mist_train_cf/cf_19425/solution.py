"""
QUESTION:
Implement a function `generate_permutations` that takes a string `s` as input and returns a list of distinct permutations of the string, without using any built-in functions or libraries to generate permutations. The function should be able to handle strings containing duplicate characters and should not generate duplicate permutations. The time complexity of the algorithm should be O(n!).
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
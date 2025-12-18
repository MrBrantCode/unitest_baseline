"""
QUESTION:
Write a function called `permute` that prints all unique permutations of the characters in a given string without using recursion. The input string can contain duplicate characters, and the function should handle these duplicates correctly.
"""

def permute(string):
    chars = list(string)
    chars.sort()
    permutations = []
    
    while True:
        permutations.append(''.join(chars))
        
        largest_i = -1
        for i in range(len(chars) - 1):
            if chars[i] < chars[i+1]:
                largest_i = i
        
        if largest_i == -1:
            break
        
        largest_j = -1
        for j in range(largest_i + 1, len(chars)):
            if chars[j] > chars[largest_i]:
                largest_j = j
        
        chars[largest_i], chars[largest_j] = chars[largest_j], chars[largest_i]
        
        chars[largest_i+1:] = chars[largest_i+1:][::-1]
    
    return list(set(permutations))
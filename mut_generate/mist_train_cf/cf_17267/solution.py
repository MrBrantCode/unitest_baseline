"""
QUESTION:
Write a function `count_vowels` that takes a string as input and returns the total number of vowels in the string, considering both uppercase and lowercase vowels and excluding vowels that occur as part of a consonant cluster. The function should run in linear time complexity.
"""

def count_vowels(string):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    clusters = {'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z', 'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z'}
    
    count = 0
    cluster_flag = False
    for char in string:
        if char in vowels:
            if not cluster_flag:
                count += 1
            cluster_flag = False
        elif char in clusters:
            cluster_flag = True
        else:
            cluster_flag = False
    
    return count
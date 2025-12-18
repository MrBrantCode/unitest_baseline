"""
QUESTION:
Write a function `longest_common_start(list1, list2)` that takes two lists of strings as input and returns the longest common starting substring of at least 3 characters that is found in any pair of strings, one from each list.
"""

def longest_common_start(list1, list2):
    longest_substring = ""
    for word1 in list1:
        for word2 in list2:
            for i in range(len(word1)):
                for j in range(len(word2)):
                    if word1[i] == word2[j]:
                        substring = ""
                        k = 0
                        while (i+k) < len(word1) and (j+k) < len(word2) and word1[i+k] == word2[j+k]:
                            substring += word1[i+k]
                            k += 1
                        if len(substring) >= 3 and len(substring) > len(longest_substring):
                            longest_substring = substring
    return longest_substring
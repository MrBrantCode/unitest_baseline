"""
QUESTION:
Write a function `find_common_substring` that takes a list of strings `words` and an integer `max_length` as input, and returns a list of lists where each sublist contains two words from the input list that have a common substring of length greater than or equal to `max_length`, along with the common substring itself and its length.
"""

def find_common_substring(words, max_length):
    result = []
    for i in range(len(words)):
        for j in range(i+1, len(words)):
            substrings = set()
            for k in range(len(words[i])):
                for l in range(len(words[j])):
                    if words[i][k] == words[j][l]:
                        m = k+1
                        n = l+1
                        substring = words[i][k]
                        while m < len(words[i]) and n < len(words[j]) and words[i][m] == words[j][n]:
                            substring += words[i][m]
                            m += 1
                            n += 1
                        if len(substring) >= max_length:
                            substrings.add(substring)
            if substrings:
                result.append([words[i], words[j], max(substrings, key=len), len(max(substrings, key=len))])
    return result
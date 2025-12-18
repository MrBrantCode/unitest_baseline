"""
QUESTION:
Implement a function `find_longest_common_substring(string1, string2)` that finds the longest common substring between two input strings. The longest common substring should consist of at least three characters and be case-sensitive. Both input strings should be alphanumeric, have a length of at least five characters each, and may contain special characters such as punctuation marks and whitespace. If there are multiple longest common substrings, return all of them in lexicographical order. The time complexity of the solution should be O(n^2), where n is the length of the longest input string.
"""

def find_longest_common_substring(string1, string2):
    max_length = 0
    end_position = 0
    longest_substrings = []
    matrix = [[0] * (len(string2) + 1) for _ in range(len(string1) + 1)]

    for i in range(1, len(string1) + 1):
        for j in range(1, len(string2) + 1):
            if string1[i-1] == string2[j-1]:
                matrix[i][j] = matrix[i-1][j-1] + 1
                if matrix[i][j] > max_length:
                    max_length = matrix[i][j]
                    end_position = (i, j)
                elif matrix[i][j] == max_length:
                    if string1[i-max_length:i] < string1[end_position[0]-max_length:end_position[0]]:
                        end_position = (i, j)
            else:
                matrix[i][j] = 0

    if max_length >= 3:
        substring = string1[end_position[0]-max_length:end_position[0]]
        longest_substrings.append(substring)

    return longest_substrings
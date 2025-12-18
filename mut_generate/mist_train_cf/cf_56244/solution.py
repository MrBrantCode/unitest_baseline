"""
QUESTION:
Develop a function `shortest_substring(input_string)` that locates and extracts the shortest substring containing all distinct characters in a given string. The function should return the shortest substring. The input string will contain only characters (no numbers or special characters) and the string can be of any length.
"""

def shortest_substring(input_string):
    distinct_characters = set(input_string)
    count_unique_chars = {}
    start = 0
    minimum_length = len(input_string)
    substring = ''

    for end in range(len(input_string)):
        char = input_string[end]
        if char not in count_unique_chars:
            count_unique_chars[char] = 1
        else:
            count_unique_chars[char] += 1

        while len(count_unique_chars) == len(distinct_characters):
            if end - start + 1 <= minimum_length:
                minimum_length = end-start+1
                substring = input_string[start:end + 1]

            start_char = input_string[start]
            if count_unique_chars[start_char] > 1:
                count_unique_chars[start_char] -= 1
            else:
                del count_unique_chars[start_char]
            start += 1

    return substring
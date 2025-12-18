"""
QUESTION:
Construct a function `shortest_subsequence(input_string)` that finds the shortest subsequence within a given string of symbols (`input_string`) that contains all distinct alphabetic units. The function should return this shortest subsequence as a string.
"""

def shortest_subsequence(input_string):
    distinct_chars = set(input_string)
    counter, unique_counter = {}, 0
    left = right = 0
    min_length = float('inf')
    min_string = None

    while(right < len(input_string)):
        if input_string[right] in distinct_chars:
            counter[input_string[right]] = counter.get(input_string[right], 0) + 1
            if counter[input_string[right]] == 1: 
                unique_counter += 1

        while(unique_counter == len(distinct_chars)): 
            if right - left + 1 < min_length: 
                min_length = right - left + 1
                min_string = input_string[left:right + 1]

            counter[input_string[left]] -= 1
            if counter[input_string[left]] == 0: 
                unique_counter -= 1
            left += 1

        right += 1

    return min_string
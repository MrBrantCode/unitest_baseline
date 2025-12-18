"""
QUESTION:
Implement a function `count_chars(input_str)` that takes a string `input_str` as input and returns a sorted list of tuples, where each tuple contains a unique character from the string and its frequency. The list should be sorted in ascending order by character. You cannot use any built-in string functions or data structures such as sets, dictionaries, or Counter.
"""

def count_chars(input_str):
    # the list of tuples where each tuple is (char, count)
    freqs = []
    for c in input_str:
        found = False
        for i, pair in enumerate(freqs):
            if pair[0] == c:
                # if we found the character, just increment its occurrence by 1
                new_pair = (c, pair[1] + 1)
                freqs[i] = new_pair
                found = True
                break
        if not found:
            # if we didn't find the character, add it to the list with occurrence 1
            freqs.append((c, 1))
    # sort by character (based on ascii value)
    freqs.sort(key=lambda x: x[0]) 
    return freqs
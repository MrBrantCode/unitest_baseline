"""
QUESTION:
Write a function called `smallest_window` that takes two strings as input, `string1` and `string2`. The function should return the smallest substring of `string1` that contains all characters of `string2` in the same relative order. If no such window exists, return an empty string. The function should have a time complexity of O(n), where n is the length of `string1`.
"""

def smallest_window(string1, string2):
    # Create a dictionary to store the count of characters in string2
    target_chars = {}
    for char in string2:
        target_chars[char] = target_chars.get(char, 0) + 1

    # Initialize variables to keep track of the window
    window_start = 0
    window_length = float('inf')
    matched_chars = 0
    start_index = 0

    # Iterate through string1
    for window_end in range(len(string1)):
        # If the current character is in the target characters dictionary, decrement its count
        if string1[window_end] in target_chars:
            target_chars[string1[window_end]] -= 1
            # If the count becomes zero, we have matched all occurrences of that character
            if target_chars[string1[window_end]] == 0:
                matched_chars += 1

        # If all characters in string2 are matched, try to minimize the window size
        while matched_chars == len(target_chars):
            # Update the minimum window length if necessary
            if window_end - window_start + 1 < window_length:
                window_length = window_end - window_start + 1
                start_index = window_start

            # Move the window start to the right
            # If the character at the start of the window is in the target characters dictionary, increment its count
            if string1[window_start] in target_chars:
                target_chars[string1[window_start]] += 1
                # If the count becomes positive, it means we need to match this character again
                if target_chars[string1[window_start]] > 0:
                    matched_chars -= 1
            window_start += 1

    # If no window is found, return an empty string
    if window_length == float('inf'):
        return ""

    # Return the smallest window
    return string1[start_index:start_index + window_length]
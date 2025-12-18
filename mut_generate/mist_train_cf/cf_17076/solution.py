"""
QUESTION:
Find the most common character in a list of strings, where the list can contain up to 1 million strings, each with a maximum length of 100 characters, and the strings are case-sensitive and can contain any printable ASCII characters. The solution should have a time complexity of O(n log n), where n is the total number of characters in all the strings combined, and a space complexity of O(n).
"""

def most_common_element(strings):
    combined_string = ''.join(strings)
    combined_string = sorted(combined_string)

    current_char = combined_string[0]
    current_count = 1
    max_char = combined_string[0]
    max_count = 0

    for ch in combined_string[1:]:
        if ch == current_char:
            current_count += 1
        else:
            if current_count > max_count:
                max_count = current_count
                max_char = current_char
            current_count = 1
            current_char = ch

    if current_count > max_count:
        max_count = current_count
        max_char = current_char

    return max_char
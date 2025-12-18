"""
QUESTION:
Format a given string into proper title case. The string may contain multiple sentences and punctuation marks. The function should correctly capitalize the first letter of each word, except for certain words that should be lowercase. The function should handle edge cases such as empty strings and strings with leading/trailing spaces. The function name should be format_title_case. 

The function should have a time complexity of O(n), where n is the length of the input string, and a space complexity of O(1), meaning it should not use any additional data structures or variables that scale with the size of the input string.
"""

def format_title_case(string):
    if not string:
        return string

    words = string.strip().split()
    small_words = ["a", "an", "the", "and", "but", "or", "for", "nor", "on", "at", "to", "from", "by", "of", "in", "with", "without"]

    for i in range(len(words)):
        if i == 0 or words[i].lower() not in small_words:
            words[i] = words[i].capitalize()

    return ' '.join(words)
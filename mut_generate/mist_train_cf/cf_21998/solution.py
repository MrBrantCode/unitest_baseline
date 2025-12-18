"""
QUESTION:
Write a function called `format_title_case` that formats a given string in proper title case. The string may contain multiple sentences and punctuation marks. The function should correctly capitalize the first letter of each word, except for certain words that should be lowercase (e.g., articles, prepositions, conjunctions). The function should also handle edge cases such as empty strings and strings with leading/trailing spaces. The function should have a time complexity of O(n), where n is the length of the input string, and a space complexity of O(1).
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
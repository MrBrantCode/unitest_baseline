"""
QUESTION:
Write a function called `format_title` that formats a given string into proper title case. The function should correctly capitalize the first letter of each word in the string, except for certain words ("a", "an", "the", "in", "on", "at", "to", "for", "by", "and", "but", "or", "nor", "with") that should be lowercase. The function should handle edge cases such as empty strings and strings with leading/trailing spaces, and return the formatted string.
"""

def format_title(title):
    # Lowercase words that should not be capitalized
    lowercase_words = ["a", "an", "the", "in", "on", "at", "to", "for", "by", "and", "but", "or", "nor", "with"]

    # Split the string into words
    words = title.split()

    # Iterate through each word and format it
    for i in range(len(words)):
        # Remove leading/trailing spaces from each word
        words[i] = words[i].strip()

        # Capitalize the first letter if it is not a lowercase word
        if i == 0 or words[i].lower() not in lowercase_words:
            words[i] = words[i].capitalize()

    # Join the words back into a string
    formatted_title = " ".join(words)

    return formatted_title
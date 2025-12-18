"""
QUESTION:
Write a function `unique_words` that takes two strings as input and returns the number of unique words in each string, the total number of unique words combining both strings, and the words that appear in both strings. The function should ignore case differences and punctuation, and should be efficient enough to handle extremely large input strings.
"""

def unique_words(string1, string2):
    # Convert all letters to lower case, remove punctuation and split the sentences
    # into list of words
    string1 = ''.join(e for e in string1.lower() if e.isalnum() or e.isspace()).split()
    string2 = ''.join(e for e in string2.lower() if e.isalnum() or e.isspace()).split()

    # Use python sets to count unique words and remove duplicates
    set1 = set(string1)
    set2 = set(string2)

    # Get intersection of sets (words appearing in both sets)
    both = set1.intersection(set2)

    return len(set1), len(set2), len(set1.union(set2)), both
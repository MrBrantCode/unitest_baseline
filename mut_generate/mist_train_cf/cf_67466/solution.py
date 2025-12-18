"""
QUESTION:
Create a function called `count_palindromes` that takes a string `paragraph` as input and returns a dictionary where the keys are the palindrome words found in the paragraph and the values are their corresponding frequencies. The function should ignore case and punctuation.
"""

def count_palindromes(paragraph):
    # Remove punctuation and convert to lower case
    clean_paragraph = ''.join(e for e in paragraph if e.isalnum() or e.isspace()).lower()
    
    # Split paragraph into words
    words = clean_paragraph.split()

    # Count palindromes
    palindrome_count = {}
    for word in words:
        # Identify palindrome
        if word == word[::-1]:
            if word in palindrome_count:
                palindrome_count[word] += 1
            else:
                palindrome_count[word] = 1

    return palindrome_count
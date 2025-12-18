"""
QUESTION:
In this problem the input will consist of a number of lines of English text consisting of the letters of the English alphabet, the punctuation marks ' (apostrophe), . (full stop), , (comma), ; (semicolon), :(colon) and white space characters (blank, newline).
Your task is print the words in the text in lexicographic order (that is, dictionary order). Each word should appear exactly once in your list. You can ignore the case (for instance, "The" and "the" are to be treated as the same word). There should be no uppercase letters in the output.
For example, consider the following candidate for the input text: 
This is a sample piece of text to illustrate this 
problem.

The corresponding output would read as:
a
illustrate
is
of
piece
problem
sample
text
this
to

-----Input format-----
- The first line of input contains a single integer $N$, indicating the number of lines in the input.
- This is followed by $N$ lines of input text.

-----Output format-----
- The first line of output contains a single integer $M$ indicating the number of distinct words in the given text. 
- The next $M$ lines list out these words in lexicographic order.

-----Constraints-----
- $1 \leq N \leq 10000$
- There are at most 80 characters in each line.
- There are at the most 1000 distinct words in the given text.

-----Sample Input-----
2
This is a sample piece of text to illustrate this 
problem. 

-----Sample Output-----
10
a
illustrate
is
of
piece
problem
sample
text
this
to
"""

def sort_words_lexicographically(text_lines):
    # Initialize an empty list to store words
    words = []
    
    # Process each line of text
    for line in text_lines:
        # Remove punctuation marks
        line = line.replace('.', '').replace("'", '').replace(',', '').replace(':', '').replace(';', '')
        # Split the line into words and convert them to lowercase
        line_words = [word.lower() for word in line.split()]
        # Add the words to the main list
        words.extend(line_words)
    
    # Remove duplicate words by converting the list to a set and back to a list
    unique_words = list(set(words))
    
    # Sort the unique words lexicographically
    sorted_words = sorted(unique_words)
    
    # Return the sorted words and the number of distinct words
    return sorted_words, len(sorted_words)
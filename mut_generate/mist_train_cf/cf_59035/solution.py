"""
QUESTION:
Create a function named `create_lexicon` that takes a string `paragraph` as input and returns a dictionary where the keys are unique words from the paragraph and the values are their frequencies of occurrence. The dictionary should be sorted in ascending alphabetical order by keys.
"""

def create_lexicon(paragraph):
    lexicon = {}
    words = paragraph.replace('.', '').split()

    for word in words:
        if word not in lexicon:
            lexicon[word] = 1
        else:
            lexicon[word] += 1

    return dict(sorted(lexicon.items()))
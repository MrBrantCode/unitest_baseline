"""
QUESTION:
Create a function named `sort_paragraph` that sorts a 2D array of strings in alphabetical order. Each sub-array represents a sentence and each item within these sub-arrays is a word. The function should sort these words both on sentence level (i.e., sort words within each sentence) and paragraph level (i.e., sort resultant sentences within the paragraph). The function should return a sorted 2D array and a string where sentences are joined with a full stop and the paragraph is joined with two line-breaks.
"""

def sort_paragraph(paragraph):
    # Sort words within each sentence
    sortedSentences = [sorted(sentence) for sentence in paragraph]
    # Sort sentences within the paragraph
    sortedParagraph = sorted(sortedSentences)

    # Join sentences with a full stop and the paragraph is joined with two line-breaks
    paragraphString = ".\n\n".join([" ".join(sentence) for sentence in sortedParagraph])

    return sortedParagraph, paragraphString
"""
QUESTION:
Implement the `word_segmentation` function, which takes two parameters: `sequence` (a string of characters) and `word_list` (a list of strings). The function should return a tuple containing the total quantity of uninterrupted and non-overlapping sub-segments present within the `sequence` and the list of identified words from these sub-segments. The sub-segments must be words from the `word_list`. The function should be case-insensitive and consider each occurrence of a word as a separate sub-segment.
"""

def word_segmentation(sequence, word_list):
    sequence = sequence.lower()
    word_list = [word.lower() for word in word_list]  # convert all words to lower case, to avoid case issues

    seg_idx = [0]
    seg_words = []

    for i in range(1,len(sequence) +1):
        for j in range(len(seg_idx)):
            #checking the sub segment is in the word list or not
            if sequence[seg_idx[j]:i] in word_list:
                seg_idx.append(i)
                seg_words.append(sequence[seg_idx[j]:i])
                break
                
    return len(seg_idx)-1, seg_words
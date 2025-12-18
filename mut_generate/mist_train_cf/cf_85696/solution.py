"""
QUESTION:
Write a function `dice_coefficient(sentence1, sentence2)` that calculates the Dice's Coefficient, a measure of text string similarity, for two given sentences. The sentences are considered as sets of words. The function should return the Dice's Coefficient, calculated as 2 * |X ∩ Y| / (|X| + |Y|), where |X ∩ Y| is the count of common words in both sentences, and |X| and |Y| are the counts of words in each sentence. The function should ignore the case of the words.
"""

def dice_coefficient(sentence1, sentence2):
    # Convert the sentences into sets of words
    set1 = set(sentence1.lower().split())
    set2 = set(sentence2.lower().split())
 
    # Find the intersection of two sets
    intersection = set1.intersection(set2)

    # Calculate Dice's Coefficient
    dice_coeff = (2. * len(intersection)) / (len(set1) + len(set2))
 
    return dice_coeff
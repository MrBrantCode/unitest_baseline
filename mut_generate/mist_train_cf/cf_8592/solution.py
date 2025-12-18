"""
QUESTION:
Create a function called `predict_next_word` that takes three parameters: `pattern`, `sentence`, and `max_distance`. The function should predict the next word in the sentence based on the given pattern and maximum distance between pattern occurrences. The predicted word should be the one with the highest frequency after the pattern occurrences within the maximum distance. If multiple words have the same highest frequency, the function should select the word that appears closest to the last occurrence of the pattern. If the pattern does not appear within the maximum distance in the sentence, the function should return a message indicating that the pattern is not found.
"""

import re

def predict_next_word(pattern, sentence, max_distance):
    words = sentence.split()
    pattern_occurrences = [m.start() for m in re.finditer(pattern, sentence)]
    occurrences_within_distance = [occurrence for occurrence in pattern_occurrences if occurrence <= max_distance]
    
    if not occurrences_within_distance:
        return "Pattern not found in sentence."
    
    word_frequencies = {}
    for occurrence in occurrences_within_distance:
        next_word_index = words.index(pattern.split()[-1], occurrence) + 1
        if next_word_index < len(words):
            next_word = words[next_word_index]
            if next_word in word_frequencies:
                word_frequencies[next_word] += 1
            else:
                word_frequencies[next_word] = 1
    
    max_frequency = max(word_frequencies.values())
    predicted_words = [word for word, frequency in word_frequencies.items() if frequency == max_frequency]
    
    last_occurrence = max(occurrences_within_distance)
    closest_word = None
    closest_distance = float('inf')
    for word in predicted_words:
        try:
            distance = words.index(word, last_occurrence) - last_occurrence
            if distance < closest_distance:
                closest_distance = distance
                closest_word = word
        except ValueError:
            continue
    
    return closest_word
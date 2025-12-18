"""
QUESTION:
Create a function named `predict_next_letter` that takes three inputs: a pattern, a string of text, and a maximum distance between pattern occurrences. The function should predict the next letter in the string of text based on the given pattern and maximum distance. The function should return the predicted letter based on frequency analysis. If multiple letters have the same highest frequency, the function should select the letter that appears closest to the last occurrence of the pattern. If the given pattern does not appear within the maximum distance in the string of text, the function should return a message indicating that the pattern is not found.
"""

def predict_next_letter(pattern, text, max_distance):
    occurrences = []
    
    # Find all occurrences of the pattern within the maximum distance
    for i in range(len(text)):
        if text[i:i+len(pattern)] == pattern:
            if len(occurrences) == 0 or (i - occurrences[-1]) <= max_distance:
                occurrences.append(i)
            else:
                break
    
    # Extract the letter that appears after each occurrence of the pattern
    letters = [text[i+len(pattern)] for i in occurrences]
    
    # Count the frequency of each letter
    frequencies = {}
    for letter in letters:
        frequencies[letter] = frequencies.get(letter, 0) + 1
    
    if len(frequencies) == 0:
        return "Pattern not found."
    
    # Find the letter with the highest frequency
    max_frequency = max(frequencies.values())
    predicted_letters = [letter for letter, freq in frequencies.items() if freq == max_frequency]
    
    # Select the letter that appears closest to the last occurrence of the pattern
    last_occurrence = occurrences[-1]
    closest_letter = predicted_letters[0]
    closest_distance = len(text)
    for letter in predicted_letters:
        distance = last_occurrence + text[last_occurrence:].find(letter)
        if distance < closest_distance:
            closest_letter = letter
            closest_distance = distance
    
    return f"Predicted letter: {closest_letter}"
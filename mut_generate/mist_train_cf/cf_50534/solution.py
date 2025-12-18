"""
QUESTION:
Create a function named `penultimate_t` that takes an array of words as input. The function should return a boolean value indicating whether any word in the array has the consonant 't' as its penultimate character and the list of such words. The function should only consider English words with a length of at least 3 characters. The function should be case-insensitive when checking for the penultimate character 't'.
"""

def penultimate_t(words):
    t_words = [word for word in words if len(word)>=3 and word[-2].lower()=='t']
    return len(t_words) > 0, t_words
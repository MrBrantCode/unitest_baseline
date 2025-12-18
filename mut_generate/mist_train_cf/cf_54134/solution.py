"""
QUESTION:
Develop a function called `vowel_analysis` that calculates the quantity of vowel phonetic sounds within a given sequence of alphabetic characters and determines the most frequently occurring vowel, considering case sensitivity and diacritic marks. The function should return the total quantity of vowels and the most frequent vowel along with its frequency. If no vowels are found, the function should return a message indicating this and `None` as the most common vowel.
"""

from collections import Counter

def vowel_analysis(txt):
    vowels = "aeiouAEIOUáéíóúÁÉÍÓÚäëïöüÄËÏÖÜ"
    vowels_in_txt = [c for c in txt if c in vowels]
    
    if not vowels_in_txt:
        return "No vowels found", None

    counter = Counter(vowels_in_txt)
    most_common = counter.most_common(1)[0]

    return len(vowels_in_txt), f"The most frequent vowel is '{most_common[0]}' with frequency {most_common[1]}"
"""
QUESTION:
Create a function named `vowel_count(sentence)` that takes a string input `sentence`. The function should count the total number of vowels and the individual count of each vowel (both lowercase and uppercase) in the sentence. It should also calculate the percentage of vowel occurrence compared to the total alphabetic characters in the sentence, ignoring non-alphabetic characters. The function should then return or print the total number of vowels, the breakdown of each vowel's count, and the percentage of total vowels.
"""

def vowel_count(sentence):
    # All vowels.
    vowels = {'A':0, 'a':0, 'E':0, 'e':0, 'I':0 ,'i':0, 'O':0, 'o':0, 'U':0, 'u':0}
    
    # Count total letters.
    total_letters = 0
    for character in sentence:
        if character.isalpha():
            total_letters += 1
            if character in vowels:
                vowels[character] += 1
                
    # Calculate total vowels.
    total_vowels = sum(vowels.values())
    
    # Calculate the percentage.
    percentage = (total_vowels / total_letters) * 100 if total_letters > 0 else 0
    
    # Return the result.
    return total_vowels, vowels, percentage
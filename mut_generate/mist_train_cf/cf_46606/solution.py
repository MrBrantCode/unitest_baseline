"""
QUESTION:
Create a function named `count_syllables(word)` that takes a word as input and returns the syllable count of the word. The function should calculate the syllables without using any existing libraries. 

Write a program that takes a list of words as input, uses the `count_syllables(word)` function to count the syllables for each word, and returns a new list with the words that have the most syllables. The program should also identify any unusual words (those that don't exist in the English dictionary) in the list and print them out with an error message. The program can use the `enchant` library to check if a word is present in the English dictionary. 

The `count_syllables(word)` function should handle cases where words end with 'e' or 'le' correctly. If a word ends with 'e', the function should decrease the syllable count only if the 'e' is silent (i.e., the character before it is not a vowel). If a word ends with 'le', the function should increase the syllable count only if the character before 'le' is not a vowel.
"""

def count_syllables(word):
    count = 0
    vowels = 'aeiouy'
    word = word.lower().strip(".:;?!")
    if word[0] in vowels:
        count +=1
    for index in range(1,len(word)):
        if word[index] in vowels and word[index-1] not in vowels:
            count +=1
    if word.endswith('e') and word[-2] not in vowels:
        count -= 1
    if word.endswith('le') and word[-3] not in vowels:
        count+=1
    if count == 0:
        count +=1
    return count
"""
QUESTION:
Write a function `reversed_words_count_vowels(sentence)` that takes a sentence as input, reverses each word while maintaining the overall word order, counts the number of vowels in each word (considering punctuation marks as part of the words and ignoring case), and returns the result.
"""

def reversed_words_count_vowels(sentence):
    words = sentence.split()  
    vowels_count = []  

    for word in words:
        count = 0
        for char in word:
            if char.lower() in 'aeiou':  
                count += 1
        vowels_count.append(count)

    reversed_words = [word[::-1] for word in words]
    return [(word, count) for word, count in zip(reversed_words, vowels_count)]
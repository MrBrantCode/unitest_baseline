"""
QUESTION:
Create a function called `solve_problem` that takes a sentence as input and returns a dictionary where the keys are the unique words in the sentence and the values are the number of vowels in each word. The function should ignore case when counting vowels, and it should consider only the standard English vowels 'a', 'e', 'i', 'o', and 'u'.
"""

def solve_problem(sentence):
    vowels = 'aeiou'
    word_list = sentence.split()
    associative_array = {}

    for word in word_list:
        vowel_count = 0
        for char in word:
            if char.lower() in vowels:
                vowel_count += 1
        associative_array[word] = vowel_count

    return associative_array
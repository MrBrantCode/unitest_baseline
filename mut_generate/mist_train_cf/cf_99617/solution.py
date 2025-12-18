"""
QUESTION:
Write a function called `sort_by_vowel_frequency` that takes a list of strings as input. The function should sort the list based on the frequency of "e" and "o" in each word, excluding words that contain the letter "x". The list should be sorted in descending order of vowel frequency. In case of a tie, the words should be sorted alphabetically.
"""

def sort_by_vowel_frequency(word_list):
    vowels = ['e', 'o']
    filtered_list = [word for word in word_list if 'x' not in word]
    frequency_dict = {}
    for word in filtered_list:
        frequency = sum([word.count(vowel) for vowel in vowels])
        if frequency not in frequency_dict:
            frequency_dict[frequency] = [word]
        else:
            frequency_dict[frequency].append(word)
    sorted_list = []
    for frequency in sorted(frequency_dict.keys(), reverse=True):
        sorted_list.extend(sorted(frequency_dict[frequency]))
    return sorted_list
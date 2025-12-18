"""
QUESTION:
Write a function `sort_by_vowel_frequency(word_list)` that sorts a list of strings based on the frequency of "e" and "o" in each word. The function should exclude words containing the letter "x" and return a list of words sorted in descending order of vowel frequency. If multiple words have the same frequency, sort them alphabetically.
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
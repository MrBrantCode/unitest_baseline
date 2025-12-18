"""
QUESTION:
Write a function `calculate_vowel_frequency` that takes an input string of up to 50 characters and returns a dictionary containing the frequency of each vowel in the string, sorted in ascending order by ASCII value. The frequency is calculated as the number of times each vowel appears in the string divided by the total number of vowels.
"""

def calculate_vowel_frequency(input_str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_ascii_dict = {}
    for char in input_str:
        if char in vowels:
            vowel_ascii_dict[char] = ord(char)

    vowel_ascii_dict_sorted = dict(sorted(vowel_ascii_dict.items(), key=lambda item: item[1]))

    vowel_count_dict = {vowel: input_str.count(vowel) for vowel in vowels}

    total_vowels = sum(vowel_count_dict.values())

    frequency_table = {}
    for vowel, count in vowel_count_dict.items():
        if total_vowels != 0:
            frequency_table[vowel] = count / total_vowels

    return frequency_table
"""
QUESTION:
Create a function `upper_case_string_and_dict_match` that takes two inputs: a string and a list of English words. Convert the entire string to uppercase and return it. Additionally, create a new string where only the words that are present in the provided list are capitalized, while the rest of the words remain in their original form. The function should return both the fully uppercase string and the partially capitalized string. The list of English words will be provided as an additional input. Ensure the function is efficient and handles the search operation in the list of words with optimal time complexity.
"""

def upper_case_string_and_dict_match(input_str, word_dict):
    upper_input_str = input_str.upper()
    str_words = input_str.split()
    capitalized_str = ' '.join(word if word not in word_dict else word.capitalize() for word in str_words)
    return upper_input_str, capitalized_str
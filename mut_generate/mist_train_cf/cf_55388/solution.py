"""
QUESTION:
Construct a function named `translate_numbers_and_lower` that takes a string `text` and a dictionary `lang_dict` as input. The function should convert all uppercase letters in `text` to their lowercase equivalents and replace any digits in `text` with their corresponding verbal expressions in a foreign language as defined in `lang_dict`. The function should also handle fractional numbers and convert them into their word counterparts. The output should be a string with the translated and lowercased text.
"""

def translate_numbers_and_lower(text, lang_dict):
    text = text.lower()
    new_text_list = []
    for word in text.split(' '):
        if word.replace('.', '').isdigit():
            if '.' in word:
                int_part, frac_part = word.split('.')
                new_word = f'{lang_dict[int(int_part)]} punto {lang_dict[int(frac_part)]}'
            else:
                new_word = lang_dict[int(word)]
            new_text_list.append(new_word)
        else:
            new_text_list.append(word)
    return ' '.join(new_text_list)
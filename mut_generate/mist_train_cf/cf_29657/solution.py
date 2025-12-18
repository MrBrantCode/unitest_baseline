"""
QUESTION:
Write a function `rearrange_and_extract_special_verse` that takes a string of song verses as input. The verses are separated by newline characters and may be prefixed with `<`, `>`, or `Portal:`. The function should rearrange the verses according to the directional indicators `<` and `>` and return the verse prefixed with `Portal:`. If a verse is prefixed with `<`, it should be inserted at the beginning of the rearranged verses, and if a verse is prefixed with `>`, it should be appended to the end of the rearranged verses. If a verse is prefixed with `Portal:`, it should be extracted and returned as the special verse.
"""

def rearrange_and_extract_special_verse(input_str):
    verses = input_str.split('\n')
    rearranged_verses = []
    special_verse = None

    for verse in verses:
        if verse.startswith('<'):
            rearranged_verses.insert(0, verse[2:])
        elif verse.startswith('>'):
            rearranged_verses.append(verse[2:])
        elif verse.startswith('Portal:'):
            special_verse = verse.split(': ', 1)[1]

    return special_verse
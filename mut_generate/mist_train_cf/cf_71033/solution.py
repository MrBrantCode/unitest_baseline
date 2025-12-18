"""
QUESTION:
Write a function called `combine_phrases` that takes a list of phrases as input and returns a single sentence where each phrase is separated by a semicolon and a space. Each phrase should be filtered to have no more than 5 words and any alphabets from numbers should be removed.
"""

def combine_phrases(lst_phrases):
    filtered_list = []
    for phrase in lst_phrases:
        words_in_phrase = phrase.split()
        if len(words_in_phrase) <= 5:
            new_phrase = ''.join([i if i.isnumeric() else '' for i in phrase])
            filtered_list.append(new_phrase)
    combined_sentence = '; '.join(filtered_list)
    return combined_sentence
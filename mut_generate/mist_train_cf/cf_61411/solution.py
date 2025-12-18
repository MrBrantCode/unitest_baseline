"""
QUESTION:
Create a function `title_case` that takes two parameters: a list of small words to ignore and a string. The function should convert the string to title case, capitalizing the first letter of each word, while ignoring the small words unless they are the first word in the string. The function should return the converted string.
"""

def title_case(smallwords, s):
    word_list = s.split()
    for i in range(len(word_list)):
        if i == 0 or word_list[i].lower() not in [small_word.lower() for small_word in smallwords]:
            word_list[i] = word_list[i].capitalize() 
        else:
            word_list[i] = word_list[i].lower()
    return ' '.join(word_list)
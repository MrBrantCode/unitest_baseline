"""
QUESTION:
Create a function `find_common_strings(help_text: str) -> List[str]` where `help_text` is a string containing the help text with a length between 1 and 10^5. The function should return a list of common strings that appear in multiple places within the text, sorted in lexicographical order, ignoring case and punctuation, and considering only alphanumeric characters.
"""

from typing import List

def find_common_strings(help_text: str) -> List[str]:
    sections = help_text.split("===")[1:]  
    words_dict = {}  

    for section in sections:
        words = section.split()  
        for word in words:
            word = word.lower().strip('.,')  
            if word.isalpha():  
                if word in words_dict:
                    words_dict[word] += 1  
                else:
                    words_dict[word] = 1  

    common_strings = [word for word, freq in words_dict.items() if freq > 1]  
    return sorted(common_strings)  
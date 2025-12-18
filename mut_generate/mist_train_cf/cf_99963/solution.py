"""
QUESTION:
Write a Python function named `add_html_tag` that takes two parameters, `sentence` and `tag`, where `sentence` is the original sentence and `tag` is the descriptive category of a specific word. The function should add HTML tags to the specific word in the sentence and return the updated sentence. The word to be tagged is "apples".
"""

def add_html_tag(sentence, tag):
    return sentence.replace("apples", f'<{tag}>apples</{tag}>')
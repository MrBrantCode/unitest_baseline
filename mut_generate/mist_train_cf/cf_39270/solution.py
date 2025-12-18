"""
QUESTION:
Implement the `weibo_tokenize` function, which takes a string of Weibo text as input where each word and its part-of-speech (POS) tag are separated by a forward slash '/'. The function should split the input text into tokens based on the whitespace delimiter, extract the word and POS tag for each token, create a WeiboToken instance for each token, and return a list of WeiboToken instances.

The function should assume the WeiboToken class is already defined with the structure: `class WeiboToken: def __init__(self, word, pos_tag): self.word = word; self.pos_tag = pos_tag`. The returned list should contain only WeiboToken instances.
"""

class WeiboToken:
    def __init__(self, word, pos_tag):
        self.word = word
        self.pos_tag = pos_tag

def weibo_tokenize(weibo_text):
    tokens = weibo_text.split()  
    weibo_tokens = []
    for token in tokens:
        word, pos_tag = token.split('/')  
        weibo_token = WeiboToken(word, pos_tag)  
        weibo_tokens.append(weibo_token)
    return weibo_tokens 
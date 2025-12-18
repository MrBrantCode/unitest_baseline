"""
QUESTION:
Write a function `find_ngram(tkns, names, optional, exclude_list)` that finds and returns a specific n-gram from a given set of names. The function should take in four parameters: `tkns` (a list of tokens representing the n-gram to be found), `names` (a dictionary containing n-grams and their corresponding tokens), `optional` (a string representing an optional parameter), and `exclude_list` (a list of tokens to be excluded from the search). The function should return the n-gram that matches the given tokens, considering the optional parameter and excluding any tokens specified in the `exclude_list`. If no matching n-gram is found, the function should return an empty string.
"""

def entance(tkns, names, optional, exclude_list):
    try:
        if not len(tkns):
            return ''

        tkns_str = ' '.join(tkns)

        for ngram, tokens in names.items():
            if tkns_str in ngram and all(token not in exclude_list for token in tokens):
                if optional in ngram:
                    return ngram

        return ''
    except Exception as e:
        return ''
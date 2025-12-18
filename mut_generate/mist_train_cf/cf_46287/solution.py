"""
QUESTION:
Implement a function `spellchecker(wordlist, queries)` that takes in a list of words `wordlist` and a list of query words `queries`. The function should return a list of corrected words, where each corrected word corresponds to the query word at the same index in the `queries` list.

The correction rules are as follows:
- If the query word exactly matches a word in `wordlist`, return the exact match.
- If the query word matches a word in `wordlist` up to capitalization, return the first match.
- If the query word matches a word in `wordlist` up to vowel errors (substituting 'a', 'e', 'i', 'o', 'u' with any vowel), return the first match.
- If no match is found, return an empty string.

The input constraints are:
- `1 <= wordlist.length, queries.length <= 5000`
- `1 <= wordlist[i].length, queries[i].length <= 7`
- `wordlist[i]` and `queries[i]` consist only of English letters.
"""

def entrance(wordlist, queries):
    def replacementVowel(word):
        return "".join('*' if c in 'aeiou' else c for c in word)
    
    word_perfect = set(wordlist)
    word_case = {word.lower(): word for word in wordlist[::-1]}
    word_vowel = {replacementVowel(word.lower()): word for word in wordlist[::-1]}
    
    def solve(query):
        if query in word_perfect:
            return query
        queryL = query.lower()
        if queryL in word_case:
            return word_case[queryL]
        queryLV = replacementVowel(queryL)
        if queryLV in word_vowel:
            return word_vowel[queryLV]
        return ""
    
    return list(map(solve, queries))
"""
QUESTION:
Implement a function named `spellchecker` that takes in two parameters: `wordlist` and `queries`. The function should return a list of words where each word corresponds to the correct spelling of the query word based on the given rules. 

The rules are as follows:
- If the query exactly matches a word in the wordlist (case-sensitive), the same word should be returned.
- If the query matches a word up to capitalization, the first such match in the wordlist should be returned.
- If the query matches a word up to vowel errors, the first such match in the wordlist should be returned.
- If the query has no matches in the wordlist, an empty string should be returned.

The input parameters have the following constraints:
- 1 <= wordlist.length, queries.length <= 5000
- 1 <= wordlist[i].length, queries[i].length <= 7
- wordlist[i] and queries[i] consist only of English letters.
"""

def spellchecker(wordlist, queries):
    def devowel(word):
        """Replace vowels with '*'."""
        return ''.join('*' if c in 'aeiou' else c for c in word)
    
    words_perfect = set(wordlist)
    words_cap = {word.lower(): word for word in reversed(wordlist)}
    words_vow = {devowel(word.lower()): word for word in reversed(wordlist)}
    
    def solve(query):
        """Find the correct spelling for a query."""
        if query in words_perfect: return query
        if query.lower() in words_cap: return words_cap[query.lower()]
        if devowel(query.lower()) in words_vow: return words_vow[devowel(query.lower())]
        return ""

    return list(map(solve, queries))
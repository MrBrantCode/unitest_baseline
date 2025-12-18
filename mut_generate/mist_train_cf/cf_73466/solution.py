"""
QUESTION:
Given a list of pairs of equivalent words `synonyms`, a sentence `text`, and a list of word frequencies `wordFreq`, return all possible synonymous sentences sorted lexicographically. The word frequencies list contains pairs of words and their corresponding frequency in the text, and the frequency of a word should not change when it is replaced by its synonym. Note that 0 <= synonyms.length <= 10, text is a single space separated sentence of at most 10 words, 0 <= wordFreq.length <= 10, and all words consist of at most 10 English letters only.
"""

from collections import defaultdict

def generateSentences(synonyms, text, wordFreq):
    # Create a dictionary to store the synonyms
    dict_syn = defaultdict(list)
    for x, y in synonyms:
        dict_syn[x].append(y)
        dict_syn[y].append(x)
            
    text_list = text.split()
    ans = set()
        
    # Perform depth first search
    def dfs(idx, path):
        if idx == len(text_list):
            ans.add(" ".join(path))
            return
        cur = text_list[idx]
        # Replace word with all possible synonyms
        subs = getSynonyms(cur)
        for j in subs: 
            dfs(idx + 1, path + [j])
            
    # Use Union Find to get all synonyms
    def getSynonyms(word):
        ans = set()
        stack = [word]
        while stack:
            w = stack.pop()
            ans.add(w)
            for j in dict_syn[w]:
                if j not in ans:
                    stack.append(j)
        return sorted(list(ans))
        
    dfs(0, [])
        
    # Return the results sorted lexicographically
    return sorted(list(ans))
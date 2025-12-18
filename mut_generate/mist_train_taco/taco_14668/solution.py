"""
QUESTION:
After you had helped Fedor to find friends in the «Call of Soldiers 3» game, he stopped studying completely. Today, the English teacher told him to prepare an essay. Fedor didn't want to prepare the essay, so he asked Alex for help. Alex came to help and wrote the essay for Fedor. But Fedor didn't like the essay at all. Now Fedor is going to change the essay using the synonym dictionary of the English language.

Fedor does not want to change the meaning of the essay. So the only change he would do: change a word from essay to one of its synonyms, basing on a replacement rule from the dictionary. Fedor may perform this operation any number of times.

As a result, Fedor wants to get an essay which contains as little letters «R» (the case doesn't matter) as possible. If there are multiple essays with minimum number of «R»s he wants to get the one with minimum length (length of essay is the sum of the lengths of all the words in it). Help Fedor get the required essay.

Please note that in this problem the case of letters doesn't matter. For example, if the synonym dictionary says that word cat can be replaced with word DOG, then it is allowed to replace the word Cat with the word doG.


-----Input-----

The first line contains a single integer m (1 ≤ m ≤ 10^5) — the number of words in the initial essay. The second line contains words of the essay. The words are separated by a single space. It is guaranteed that the total length of the words won't exceed 10^5 characters.

The next line contains a single integer n (0 ≤ n ≤ 10^5) — the number of pairs of words in synonym dictionary. The i-th of the next n lines contains two space-separated non-empty words x_{i} and y_{i}. They mean that word x_{i} can be replaced with word y_{i} (but not vise versa). It is guaranteed that the total length of all pairs of synonyms doesn't exceed 5·10^5 characters.

All the words at input can only consist of uppercase and lowercase letters of the English alphabet.


-----Output-----

Print two integers — the minimum number of letters «R» in an optimal essay and the minimum length of an optimal essay.


-----Examples-----
Input
3
AbRb r Zz
4
xR abRb
aA xr
zz Z
xr y

Output
2 6

Input
2
RuruRu fedya
1
ruruRU fedor

Output
1 10
"""

import collections

def optimize_essay(m, essay, n, synonyms):
    # Convert all words to lowercase
    essay = [word.lower() for word in essay]
    synonyms = [(word1.lower(), word2.lower()) for word1, word2 in synonyms]
    
    # Create a dictionary to map words to unique indices
    sti = dict()
    pack = lambda word: (word.count('r'), len(word), sti.setdefault(word, len(sti)))
    
    # Create a defaultdict to store edges between synonyms
    edge = collections.defaultdict(list)
    nodes = list()
    
    # Process each synonym pair
    for word, synon in synonyms:
        word_packed = pack(word)
        synon_packed = pack(synon)
        edge[synon_packed[-1]].append(word_packed[-1])
        nodes.append(word_packed)
        nodes.append(synon_packed)
    
    # Sort nodes based on the number of 'r's and length
    nodes.sort()
    
    # Dictionary to store the best (minimum 'r' count, minimum length) for each node
    best = dict()
    
    # Process each node to find the best replacement
    for node in nodes:
        if node[2] not in best:
            stack = [node[2]]
            while stack:
                top = stack.pop()
                if top not in best:
                    best[top] = node[:2]
                    for n in edge[top]:
                        if n not in best:
                            stack.append(n)
    
    # Calculate the total 'r' count and length of the optimized essay
    tr = 0
    tl = 0
    for word in essay:
        if word in sti:
            wid = sti[word]
            tr += best[wid][0]
            tl += best[wid][1]
        else:
            tr += word.count('r')
            tl += len(word)
    
    return tr, tl
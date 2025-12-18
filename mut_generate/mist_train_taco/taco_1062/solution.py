"""
QUESTION:
In English, we have a concept called root, which can be followed by some other words to form another longer word - let's call this word successor. For example, the root an, followed by other, which can form another word another.




Now, given a dictionary consisting of many roots and a sentence. You need to replace all the successor in the sentence with the root forming it. If a successor has many roots can form it, replace it with the root with the shortest length.



You need to output the sentence after the replacement.



Example 1:

Input: dict = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"




Note:

The input will only have lower-case letters.
 1 
 1 
 1 
 1
"""

def replace_words_in_sentence(roots, sentence):
    def build_trie(roots):
        trie = {}
        for word in roots:
            current = trie
            for char in word:
                if char not in current:
                    current[char] = {}
                current = current[char]
            current['#'] = word
        return trie

    def find_root(word, trie):
        current = trie
        for char in word:
            if char not in current:
                break
            current = current[char]
            if '#' in current:
                return current['#']
        return word

    trie = build_trie(roots)
    words = sentence.split()
    replaced_words = [find_root(word, trie) for word in words]
    return ' '.join(replaced_words)
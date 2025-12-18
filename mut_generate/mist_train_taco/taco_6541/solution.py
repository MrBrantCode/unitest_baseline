"""
QUESTION:
You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

Example 1:


Input:
s = "barfoothefoobarman",
words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.


Example 2:


Input:
s = "wordgoodstudentgoodword",
words = ["word","student"]
Output: []
"""

def find_substring_indices(s: str, words: list) -> list:
    if not s or not words:
        return []
    
    len_str = len(s)
    len_word = len(words[0])
    len_substr = len(words) * len_word
    word_count = {}
    
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    result = []
    
    for i in range(min(len_word, len_str - len_substr + 1)):
        find_answer(i, len_str, len_word, len_substr, s, word_count, result)
    
    return result

def find_answer(str_start: int, len_str: int, len_word: int, len_substr: int, s: str, word_count: dict, result: list):
    word_start = str_start
    current_count = {}
    
    while str_start + len_substr <= len_str:
        word = s[word_start:word_start + len_word]
        word_start += len_word
        
        if word not in word_count:
            str_start = word_start
            current_count.clear()
        else:
            if word in current_count:
                current_count[word] += 1
            else:
                current_count[word] = 1
            
            while current_count[word] > word_count[word]:
                current_count[s[str_start:str_start + len_word]] -= 1
                str_start += len_word
            
            if word_start - str_start == len_substr:
                result.append(str_start)
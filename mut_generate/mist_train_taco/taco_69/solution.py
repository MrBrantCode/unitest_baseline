"""
QUESTION:
Given a dictionary of words and a pattern. Every character in the pattern is uniquely mapped to a character in the dictionary. Find all such words in the dictionary that match the given pattern. 
Example 1:
Input:
N = 4
dict[] = {abb,abc,xyz,xyy}
pattern  = foo
Output: abb xyy
Explanation: xyy and abb have the same
character at index 1 and 2 like the
pattern.
Your Task:
You don't need to read input or print anything. Your task is to complete the function findMatchedWords() which takes an array of strings dict[] consisting of the words in the dictionary and a string, Pattern and returns an array of strings consisting of all the words in the dict[] that match the given Pattern in lexicographical order.
Expected Time Complexity: O(N*K) (where K is the length of the pattern).
Expected Auxiliary Space: O(N).
Constraints:
1 <= N <= 10
"""

def find_matched_words(dict_list, pattern):
    def is_match(word, pattern):
        if len(word) != len(pattern):
            return False
        char_map = {}
        used_chars = set()
        for w_char, p_char in zip(word, pattern):
            if w_char in char_map:
                if char_map[w_char] != p_char:
                    return False
            else:
                if p_char in used_chars:
                    return False
                char_map[w_char] = p_char
                used_chars.add(p_char)
        return True

    matched_words = [word for word in dict_list if is_match(word, pattern)]
    return sorted(matched_words)
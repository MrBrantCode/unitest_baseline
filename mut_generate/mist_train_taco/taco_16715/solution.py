"""
QUESTION:
Smith wakes up at the side of a dirty, disused bathroom, his ankle chained to pipes. Next to him is tape-player with a hand-written message "Play Me". He finds a tape in his own back pocket. After putting the tape in the tape-player, he sees a key hanging from a ceiling, chained to some kind of a machine, which is connected to the terminal next to him. After pressing a Play button a rough voice starts playing from the tape:

"Listen up Smith. As you can see, you are in pretty tough situation and in order to escape, you have to solve a puzzle. 

You are given N strings which represent words. Each word is of the maximum length L and consists of characters 'a'-'e'. You are also given M strings which represent patterns. Pattern is a string of length  ≤ L and consists of characters 'a'-'e' as well as the maximum 3 characters '?'. Character '?' is an unknown character, meaning it can be equal to any character 'a'-'e', or even an empty character. For each pattern find the number of words that matches with the given pattern. After solving it and typing the result in the terminal, the key will drop from the ceiling and you may escape. Let the game begin."

Help Smith escape.

Input

The first line of input contains two integers N and M (1 ≤ N ≤ 100 000, 1 ≤ M ≤ 5000), representing the number of words and patterns respectively.

The next N lines represent each word, and after those N lines, following M lines represent each pattern. Each word and each pattern has a maximum length L (1 ≤ L ≤ 50). Each pattern has no more that three characters '?'. All other characters in words and patters are lowercase English letters from 'a' to 'e'.

Output

Output contains M lines and each line consists of one integer, representing the number of words that match the corresponding pattern.

Example

Input

3 1
abc
aec
ac
a?c


Output

3

Note

If we switch '?' with 'b', 'e' and with empty character, we get 'abc', 'aec' and 'ac' respectively.
"""

from itertools import product
from collections import defaultdict

def count_matching_words(words, patterns):
    # Create a dictionary to count occurrences of each word
    word_count = defaultdict(int)
    for word in words:
        word_count[word] += 1
    
    # List of possible characters
    tb = ['a', 'b', 'c', 'd', 'e']
    
    # Function to perform depth-first search for pattern matching
    def dfs(pattern, l, u, res, st, word_count):
        if u == l:
            if res in st:
                return 0
            if res in word_count:
                return word_count[res]
            return 0
        
        cnt = 0
        if pattern[u] == '?':
            for i in range(6):
                if i != 5:
                    cnt += dfs(pattern, l, u + 1, res + tb[i], st, word_count)
                else:
                    cnt += dfs(pattern, l, u + 1, res, st, word_count)
        else:
            cnt += dfs(pattern, l, u + 1, res + pattern[u], st, word_count)
        
        return cnt
    
    # Result list to store the count of matching words for each pattern
    result = []
    
    # Process each pattern
    for pattern in patterns:
        l = len(pattern)
        st = set()
        cnt = dfs(pattern, l, 0, '', st, word_count)
        result.append(cnt)
    
    return result
"""
QUESTION:
You are given an array of words where each word consists of lowercase English letters.
word_{A} is a predecessor of word_{B} if and only if we can insert exactly one letter anywhere in word_{A} without changing the order of the other characters to make it equal to word_{B}.
	For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".
A word chain is a sequence of words [word_{1}, word_{2}, ..., word_{k}] with k >= 1, where word_{1} is a predecessor of word_{2}, word_{2} is a predecessor of word_{3}, and so on. A single word is trivially a word chain with k == 1.
Return the length of the longest possible word chain with words chosen from the given list of words.
Example 1:
Input:
n = 6
words = ["a","b","ba","bca","bda","bdca"]
Output:
4
Explanation:
One of the longest word chains is ["a","ba","bda","bdca"].
Example 2:
Input:
n = 2
words = ["abcd","dbqca"]
Output:
1
Explanation:
The trivial word chain ["abcd"] is one of the longest word chains.
Your Task:
You don't need to read input or print anything. Your task is to complete the function longestChain() which takes integer n and an array of words and returns the size of longest possible word chain.
Expected Time Complexity: O( n * n * L),where L is the length of the longest string in the words.
Expected Space Complexity: O(n)
Constraint:
1 <= n <= 1000
1 <= words[i].length <= 16
 words[i] only consists of lowercase English letters.
"""

def longest_word_chain(words):
    def is_predecessor(word1, word2):
        if len(word1) != len(word2) + 1:
            return False
        (i, j) = (0, 0)
        while i < len(word1):
            if j < len(word2) and word1[i] == word2[j]:
                i += 1
                j += 1
            else:
                i += 1
        return i == len(word1) and j == len(word2)

    n = len(words)
    dp = [1] * n
    max_length = 1
    words.sort(key=len)

    for i in range(1, n):
        for j in range(i):
            if is_predecessor(words[i], words[j]) and 1 + dp[j] > dp[i]:
                dp[i] = 1 + dp[j]
                if max_length < dp[i]:
                    max_length = dp[i]

    return max_length
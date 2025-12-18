"""
QUESTION:
Read problems statements in Mandarin chinese, Russian and Vietnamese as well. 

Sheokand loves strings. Chef has $N$ strings $S_{1}, S_{2}, \dots, S_{N}$ which he wants to give to Sheokand; however, he doesn't want to give them away for free, so Sheokand must first correctly answer $Q$ queries Chef asks him.

In each query, Chef tells Sheokand an integer $R$ and a string $P$. Consider Chef's strings $S_{1}$ through $S_{R}$. Out of these strings, consider all strings such that their longest common prefix with $P$ is maximum possible. Sheokand should find the lexicographically smallest of these strings.

Sheokand is busy with his exams. Can you solve the queries for him?

------  Input ------
The first line of the input contains a single integer $N$.
$N$ lines follow. For each valid $i$, the $i$-th of these lines contains Chef's string $S_{i}$.
The next line contains a single integer $Q$.
The following $Q$ lines describe queries. Each of these lines contains an interger $R$, followed by a space and a string $P$.

------  Output ------
For each query, print a single line containing the string that satisfies the required conditions — the answer to that query.

------  Constraints  ------
$1 ≤ N ≤ 100,000$ 
$1 ≤ |S_{i}| ≤ 10$ for each valid $i$
$1 ≤ Q ≤ 100,000$
$1 ≤ R ≤ N$
$1 ≤ |P| ≤ 10$

------  Subtasks ------
Subtask #1 (30 points): $1 ≤ N, R ≤ 1,000$

Subtask #2 (70 points): original constraints

----- Sample Input 1 ------ 
4
abcd
abce
abcdex
abcde
3
3 abcy
3 abcde
4 abcde
----- Sample Output 1 ------ 
abcd
abcdex
abcde
----- explanation 1 ------ 
Query 1: For strings $S_{1}$ through $S_{3}$, the longest common prefix is always "abc", but "abcd" is the lexicographically smallest of these three strings.

Query 2: For strings $S_{1}$ through $S_{3}$, the longest common prefix with maximum length is "abcde" and the only string for which it is the LCP is "abcdex", so this is the answer.

Query 3: For strings $S_{1}$ through $S_{4}$, the longest common prefix with maximum length is "abcde"; it is the LCP for strings "abcdex" and "abcde", but "abcde" is the lexicographically smaller string, so it is the answer.
"""

from collections import defaultdict

def find_lexicographically_smallest_string(strings, queries):
    TrieNode = lambda: defaultdict(TrieNode)
    trie = TrieNode()
    trie['idx'] = 0

    def insert(w, cur, idx):
        for c in w:
            if c not in cur:
                cur = cur[c]
                cur['idx'] = idx
            else:
                cur = cur[c]
        cur['isWord'] = True
        if '$' not in cur:
            cur['$'] = idx

    def search(word, cur, idx):
        for i in word:
            if i not in cur or cur[i]['idx'] > idx:
                break
            pre = cur
            cur = cur[i]
        while True:
            a = []
            if cur['isWord'] and cur['$'] <= idx:
                return cur['$']
            else:
                for i in 'abcdefghijklmnopqrstuvwxyz':
                    if i in cur and cur[i]['idx'] <= idx:
                        a.append(i)
                a.sort()
                cur = cur[a[0]]

    # Insert all strings into the trie
    for idx, word in enumerate(strings):
        insert(word, trie, idx)

    # Process each query
    results = []
    for idx, p in queries:
        idx = int(idx) - 1
        result_idx = search(p, trie, idx)
        results.append(strings[result_idx])

    return results